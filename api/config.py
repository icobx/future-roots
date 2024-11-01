import pathlib

import pandas as pd
import geopandas as gpd

from enum import Enum

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

class Status(Enum):
    STARTED = "started"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

PADDING_CONFIG = {
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
        'zahon': 0.01,
        'kriky': 0.01,
        'zivy_plot': 0.01,
        'skupina_stromov': 5.0,
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

LAYERS = [
    ('roads', 'roads_ba_ruzinov'),
    ('buildings', 'buildings_ruzinov_no_points'),
    ('utilities', 'combined_utilities_ba2'),
    ('other_green_areas', 'ruzinov_zelenePlochy_ostatne'),
    ('pavements', 'ruzinov_pavements'),
    ('trees_not_over_utilities', 'trees_not_over_utilities'),
    ('trees_over_utilities', 'trees_over_utilities'),
]

MASTER_DATA_FN = 'ruzinov_zelen_in_majetok'
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



