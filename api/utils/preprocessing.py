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


def compute_trees_over_utilities(gdf_trees, gdf_utilities):
    """Compute trees that overlap and don't overlap with utility networks."""
    if 'index_right' in gdf_trees.columns:
        gdf_trees = gdf_trees.drop(['index_right'], axis=1)
    gdf_trees = gdf_trees.to_crs("EPSG:4326")
    gdf_utilities = gdf_utilities.to_crs("EPSG:4326")

    new_crs = gdf_utilities.to_crs(epsg=6933)
    new_crs['geometry'] = new_crs.buffer(0.5)
    gdf_utilities_with_buffer = new_crs.to_crs(epsg=4326)

    joined_gdf = gdf_trees.sjoin(gdf_utilities_with_buffer,predicate='intersects', how='left')
    trees_over_utilities = joined_gdf[~joined_gdf['utility'].isnull()].drop(['index_right', 'utility'], axis=1).drop_duplicates()
    trees_not_over_utilities = joined_gdf[joined_gdf['utility'].isnull()].drop(['index_right', 'utility'], axis=1).drop_duplicates()
    return trees_over_utilities, trees_not_over_utilities