import geopandas as gpd


def clip_polygons(gdf_polygons, gdf_clip_mask):
    """Perform spatial join between polygon data and clipping mask."""
    gdf_polygons = gdf_polygons.to_crs(epsg=4326)
    gdf_intersection = gpd.sjoin(left_df=gdf_polygons, right_df=gdf_clip_mask, how='inner')
    return gdf_intersection


def remove_unwanted_objects(gdf_objects):
    """Remove unwanted shapely objects from a GDF. We keep only polygons."""
    return gdf_objects[gdf_objects.geometry.apply(lambda x: x.geom_type in ['Polygon', 'MultiPolygon'])]


def add_buffer_to_polygon(gdf, buffer):
    """Add a padding of `buffer` meters to each polygon in the gdf's geometry."""
    gdf_processed = gdf.to_crs(epsg=3857)
    gdf_processed['geometry_buffer'] = gdf_processed.geometry.buffer(buffer, cap_style='square')
    gdf_processed = gdf_processed.set_geometry('geometry_buffer').to_crs(epsg=4326)
    return gdf_processed
