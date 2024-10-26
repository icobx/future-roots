import geopandas as gpd
import os


def overlay_layers(master_data, root, padding_config, layers):
    """Overlay all layers together.
    This function reads a layer, applies row-wise padding, and computes the difference between
    master_data and current layer.
    We iterate over all available layers currently and store just the final result."""
    for layer in layers:
        data = gpd.read_file(os.path.join(root, f'{layer}.geojson'))
        # After Laco is finished, replace below with data['buffer_distance'] = assign_padding(data, padding_config)
        data['buffer_distance'] = 1.0
        # Switch to 6933 to be able to compute buffers
        data = data.to_crs(epsg=6933)
        data['geometry'] = data.apply(lambda row: row.geometry.buffer(row['buffer_distance']), axis=1)
        # Switch back to the right EPSG
        data = data.to_crs(epsg=4326)
        # Compute the difference
        master_data = gpd.overlay(df1=master_data, df2=data, how='difference')
    return master_data


def apply_buffer_from_config(config):
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


def add_buffer_column(gdf, buffer_df, category_name):
    # Determine whether this category is straightforward (buildings, roads, pavements) or needs lookup
    if category_name in ['buildings', 'roads', 'pavements']:
        # Directly match on the category name for straightforward cases
        buffer_value = buffer_df.loc[buffer_df['Category'] == category_name, 'Buffer_Value'].values[0]
        gdf['buffer'] = buffer_value
    else:
        # For categories requiring lookups on 'TYP_ID' or 'utility' column
        if category_name == 'utilities':
            lookup_column = 'utility'
        elif category_name in ['other_green_areas', 'trees']:
            lookup_column = 'TYP_ID'
        else:
            raise ValueError("Invalid category name for buffer assignment.")

        # Create buffer values by joining based on specific formatted keys from buffer_df
        gdf['buffer'] = gdf[lookup_column].apply(lambda x: buffer_df.loc[buffer_df['Category'] == f"{category_name}_{x}", 'Buffer_Value'].values[0] if f"{category_name}_{x}" in buffer_df['Category'].values else None)

    return gdf