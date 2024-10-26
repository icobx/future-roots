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