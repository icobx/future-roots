import pandas as pd
import geopandas as gpd

padding_config = {
    'buildings': {
        'budovy': 2.0,
    },
    'utilities': {
        'kolektory': 1.0,
        'produktovod': 1.0,
        'produktovody_prvky': 1.0,
        'prvky_elektriny': 1.0,
        'prvky_produktovodov': 1.0,
        'prvky_telekomunikacii': 1.0,
        'prvky_vodovodnej_siete': 1.5,
        'telekomunikacie': 1.5,
        'vodovody': 2,
    },
    'other_green_areas': {
        'zahon': 1.0,
        'kriky': 1.0,
        'zivy_plot': 1.0,
        'skupina_stromov': 1.0,
        'ina_plocha_zelene': 1.0,
    },
    'roads': {
        'cesty': 1.0,
    },
    'pavements': {
        'chodniky': 1.0,
    },
    'trees': {
        '0_4m': 1.0,
        '4_10m': 3.0,
        '10_100m': 5.0,
    }
}
# buildings = gpd.read_file("buildings_ruzinov_no_points.geojson")
# utilities = gpd.read_file("combined_utilities_ba2.geojson")
#
# buildings = add_buffer_column(buildings, df, 'buildings')
# utilities = add_buffer_column(utilities, df, 'utilities')
#
# print(buildings['buffer'].unique())
# print(utilities['buffer'].unique())
#
# nan_rows = utilities[utilities['buffer'].isna()]
# print(nan_rows['utility'].unique())

# kazda ina siet ma vlastne obmedzenia
# STN ochranne pasma inzinierskych sieti
# plynovod teplovod vodovod musia byt dodrzane high priority
# vysoke napatie tiez high priority
# arboricky standard vysadby
# najst strom v tesnom kontakte s inz sietami
# vodovod - 1.5-5
# plynovod 1m
# opticke kable 1m
# zapadoslovenska dstribucna
# ochranne pasmo par 43 zakon o energetike



