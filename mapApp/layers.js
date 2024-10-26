import VectorTileLayer from "ol/layer/VectorTile";
import VectorTileSource from "ol/source/VectorTile";
import MVT from "ol/format/MVT";
import {config} from "./app.config";

export const buildingsLayer = new VectorTileLayer({
    source: new VectorTileSource({
        format: new MVT(),
        url: config.layers.buildings.path + '/{z}/{x}/{y}.pbf', // replace with your tile server URL
    }),
    minZoom: config.layers.buildings.minZoom,
    style: config.layers.buildings.style
});
buildingsLayer.set('name', 'buildings');

export const parcelsLayer = new VectorTileLayer({
    source: new VectorTileSource({
        format: new MVT(),
        url: config.layers.parcels.path + '/{z}/{x}/{y}.pbf', // replace with your tile server URL
    }),
    className: 'parcels',
    minZoom: config.layers.parcels.minZoom,
    style: config.layers.parcels.style
});
parcelsLayer.set('name', 'parcels');

export const roadsLayer = new VectorTileLayer({
    source: new VectorTileSource({
        format: new MVT(),
        url: config.layers.roads.path + '/{z}/{x}/{y}.pbf', // replace with your tile server URL
    }),
    className: 'roads',
    minZoom: config.layers.roads.minZoom,
    style: config.layers.roads.style
});
roadsLayer.set('name', 'roads');

export const greenAreasLayer = new VectorTileLayer({
    source: new VectorTileSource({
        format: new MVT(),
        url: config.layers.greenAreas.path + '/{z}/{x}/{y}.pbf', // replace with your tile server URL
    }),
    className: 'greenAreas',
    minZoom: config.layers.greenAreas.minZoom,
    style: config.layers.greenAreas.style
});
greenAreasLayer.set('name', 'greenAreas');

export const utilitiesLayer = new VectorTileLayer({
    source: new VectorTileSource({
        format: new MVT(),
        url: config.layers.utilities.path + '/{z}/{x}/{y}.pbf', // replace with your tile server URL
    }),
    className: 'utilities',
    minZoom: config.layers.utilities.minZoom,
    style: config.layers.utilities.style
});
utilitiesLayer.set('name', 'utilities');