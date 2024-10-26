import fiona
import geopandas as gpd
import os
import pandas as pd

from utils.preprocessing import clip_polygons

def process_gpkg(path: str) -> pd.DataFrame:
    layer_names = fiona.listlayers(path)
    layers_dict = {}
    for layer_name in layer_names:
        layers_dict[layer_name] = gpd.read_file(path, layer=layer_name).to_crs(epsg=4326)

    geometries = []
    for name, layer in layers_dict.items():
        if 'geometry' in layer.columns:
            layer['layerName'] = name
            geometries.append(layer[['layerName', 'geometry']])

    geometries = pd.concat(geometries)
    geometries = geometries[~pd.isnull(geometries.geometry)]
    return geometries


def process_gml(path: str) -> pd.DataFrame:
    gml_all = []
    for f in os.listdir(path):
        if f.endswith('.gml'):
            _path = os.path.join(path, f)
            layers = fiona.listlayers(_path)
            if 'CadastralParcel' in layers:
                layer = gpd.read_file(_path, layer='CadastralParcel')[['geometry']]
                gml_all.append(layer)
    gml_all = pd.concat(gml_all)
    return gml_all


if __name__ == '__main__':

    # Source files are downloaded from: h
    # https://www.geoportal.sk/sk/inspire/udaje-stiahnutie/

    print('Preprocessing roads...')
    roads = process_gpkg('../data/raw/INSPIRE_TN.gpkg')
    roads.to_file('../data/processed/all/roads.geojson', driver='GeoJSON')

    print('Preprocessing buildings...')
    buildings = process_gpkg('../data/raw/INSPIRE_BU.gpkg')
    buildings.to_file('../data/processed/all/buildings.geojson', driver='GeoJSON')

    print('Preprocessing parcels C...')
    parcels_c = process_gml('../data/raw/BratislavskyC')
    parcels_c.to_file('../data/processed/ba/parcels_c.geojson', driver='GeoJSON')

    print('Preprocessing parcels E...')
    parcels_e = process_gml('../data/raw/BratislavskyE')
    parcels_e.to_file('../data/processed/ba/parcels_e.geojson', driver='GeoJSON')