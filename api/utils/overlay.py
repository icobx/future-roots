import asyncio

import pandas as pd
import geopandas as gpd

from api.config import PROJECT_ROOT, PADDING_CONFIG, MASTER_DATA_FN, LAYERS
from api.config import Status

from concurrent.futures import ProcessPoolExecutor

def overlay_layer(
    padding_config: dict[dict[str, float]],
    master_data: gpd.GeoDataFrame,
    category_name: str,
    layer: str,
):
    file_path = PROJECT_ROOT / 'data' / 'processed' / f'{layer}.geojson'
    data = gpd.read_file(file_path)
    buffer_df = apply_buffer_from_config(padding_config=padding_config)
    data = add_buffer_column(gdf=data, buffer_df=buffer_df, category_name=category_name, padding_config=padding_config)
    # Switch to 6933 to be able to compute buffers
    data = data.to_crs(epsg=6933)
    data['geometry'] = data.apply(lambda row: row.geometry.buffer(row['buffer']), axis=1)
    # Switch back to the right EPSG
    data = data.to_crs(epsg=4326)
    # Compute the difference
    master_data = gpd.overlay(df1=master_data, df2=data, how='difference')
    if category_name == 'trees_not_over_utilities':
        master_data = calculate_area_of_polygon_squared_meters(gdf=master_data, name_of_area_column='available_area_utility_trees_gone')

    return master_data
    

async def overlay_layers(
    padding_config: dict[dict[str, float]],
    task_id: str,
    process_status: dict[tuple[Status | str]]
):
    """Overlay all layers together.
    This function reads a layer, applies row-wise padding, and computes the difference between
    master_data and current layer.
    We iterate over all available layers currently and store just the final result."""
    process_status[task_id] = (Status.STARTED, f'Task {task_id} started.')

    output_path = PROJECT_ROOT / 'data' / 'layers' / f'{task_id}.geojson'
    master_data = gpd.read_file(PROJECT_ROOT / 'data' / 'processed' / f'{MASTER_DATA_FN}.geojson')
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        for category_name, layer in LAYERS:
            process_status[task_id] = (Status.RUNNING, f'Processing {category_name} layer.')

            master_data = await loop.run_in_executor(
                executor,
                overlay_layer,
                padding_config,
                master_data,
                category_name,
                layer,
                task_id,
                process_status
            )
            process_status[task_id] = (Status.RUNNING, f'Processed {category_name} layer.')

        master_data = await loop.run_in_executor(executor, calculate_area_of_polygon_squared_meters, master_data, 'available_area_utility_trees_intact')

    master_data.to_file(output_path, driver="GeoJSON")
    process_status[task_id] = (Status.COMPLETED, f'Layers for task {task_id} overlayed.')

    return output_path


def apply_buffer_from_config(padding_config):
    # Create list to store data in the specified format
    data = []

    # Iterate through the config dictionary
    for category, subcategories in padding_config.items():
        for subcategory, value in subcategories.items():
            # Create column name
            if category in ['buildings', 'roads', 'pavements']:
                column_name = category
            else:
                column_name = f"{category}_{subcategory}"

            # Append the data as a list of tuples
            data.append((column_name, value))

    # Create DataFrame from the data list
    df = pd.DataFrame(data, columns=['Category', 'Buffer_Value'])
    return df


def add_buffer_column(gdf, buffer_df, category_name, padding_config):
    # Determine whether this category is straightforward (buildings, roads, pavements) or needs lookup
    if category_name in ['buildings', 'roads', 'pavements']:
        # Directly match on the category name for straightforward cases
        buffer_value = buffer_df.loc[buffer_df['Category'] == category_name, 'Buffer_Value'].values[0]
        gdf['buffer'] = buffer_value
    else:
        # For categories requiring lookups on 'TYP_ID' or 'utility' column
        if category_name == 'utilities':
            lookup_column = 'utility'
        elif category_name in ['other_green_areas']:
            lookup_column = 'TYP_ID'
        elif category_name in ['trees_not_over_utilities', 'trees_over_utilities']:
            category_name = 'trees'
            bins = [0, 4, 10, 100]
            labels = ['0_4m', '4_10m', '10_100m']
            gdf['binned'] = pd.cut(gdf['VYSKA_7'], bins=bins, labels=labels)
            lookup_column = 'binned'
        else:
            raise ValueError("Invalid category name for buffer assignment.")

        # Create buffer values by joining based on specific formatted keys from buffer_df
        mapping_dict = padding_config[category_name]
        mapping_df = pd.DataFrame.from_dict(mapping_dict, orient='index').reset_index()
        mapping_df = mapping_df.rename({'index': lookup_column, 0: 'buffer'}, axis=1)
        gdf = pd.merge(left=gdf, right=mapping_df, how='left', on=[lookup_column])
        gdf['buffer'] = gdf['buffer'].fillna(1.0)
    return gdf


def calculate_area_of_polygon_squared_meters(gdf, name_of_area_column='area'):
    new_crs = gdf.to_crs(epsg=6933)
    gdf[name_of_area_column] = new_crs.area
    return gdf
