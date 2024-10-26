import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import {transform} from 'ol/proj';

import {
    buildingsLayer,
    parcelsLayer,
    roadsLayer,
    greenAreasLayer,
    utilitiesLayer,
    resultLayer,
    pavementsLayer, propertiesLayer, treesLayer, baseLayer
} from './layers';

const center = [17.153015431601077, 48.162629353115584]
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
        baseLayer,
        buildingsLayer,
        parcelsLayer,
        roadsLayer,
        pavementsLayer,
        propertiesLayer,
        treesLayer,
        greenAreasLayer,
        utilitiesLayer,
        resultLayer,
    ],
    view: new View({
        center: reprojectedCenter,
        zoom: 13,
        projection: 'EPSG:3857'
    })
});

function toggleVisibility(eventsender, name) {
    map.getLayers().getArray().forEach(layer => {
        if (layer.get('name') === name) {
            if (eventsender.checked === true) {
                layer.setVisible(true);
            } else {
                layer.setVisible(false);
            }
        }
    });
}
window.toggleVisibility = toggleVisibility;

