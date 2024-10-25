import './style.css';
import {Map, View} from 'ol';
import GeoJSON from 'ol/format/GeoJSON';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import OSM from 'ol/source/OSM';
import {transform} from 'ol/proj';

const center = [17.107643281793944, 48.14530116324848]
const sourceProjection = 'EPSG:4326';
const destinationProjection = 'EPSG:3857';
const reprojectedCenter = transform(
    center,
    sourceProjection,
    destinationProjection
);


const map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: new OSM()
        }),
        new VectorLayer({
            projection: 'EPSG:4326',
            source: new VectorSource({
                url: 'http://127.0.0.1:8080/data/processed/ba_admin_unit.geojson',
                format: new GeoJSON()
            })
        })
    ],
    view: new View({
        center: reprojectedCenter,
        zoom: 10,
        projection: 'EPSG:4326'
    })
});

