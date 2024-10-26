import geopandas as gpd

from utils.preprocessing import clip_polygons


if __name__ == '__main__':
    polygon_mask = gpd.read_file('../data/processed/entire_bratislava_bounding_box.geojson')

    roads = gpd.read_file('../data/processed/roads.geojson')
    buildings = gpd.read_file('../data/processed/buildings.geojson')
    parcels_c = gpd.read_file('../data/processed/parcels_c.geojson')
    parcels_e = gpd.read_file('../data/processed/parcels_e.geojson')

    print('Clipping roads...')
    buildings_clipped = clip_polygons(roads, polygon_mask)
    buildings_clipped.to_file('../data/processed/ba/roads.geojson', driver='GeoJSON')

    print('Clipping buildings...')
    buildings_clipped = clip_polygons(buildings, polygon_mask)
    buildings_clipped.to_file('../data/processed/ba/buildings.geojson', driver='GeoJSON')

    print('Clipping parcels C...')
    parcels_e_clipped = clip_polygons(parcels_c, polygon_mask)
    parcels_e_clipped.to_file('../data/processed/ba/parcels_c.geojson', driver='GeoJSON')

    print('Clipping parcels E...')
    parcels_e_clipped = clip_polygons(parcels_e, polygon_mask)
    parcels_e_clipped.to_file('../data/processed/ba/parcels_e.geojson', driver='GeoJSON')