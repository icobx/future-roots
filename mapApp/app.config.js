export const config = {
    "layers": {
        "buildings": {
            "path": "http://localhost:8080/data/buildings",
            "minZoom": 14,
            "style": {
                "fill-color": "rgba(137, 196, 244, 0.5)"
            }
        },
        "parcels": {
            "path": "http://localhost:8080/data/parcels",
            "minZoom": 15,
            "style": {
                "stroke-color": "black",
                "stroke-width": 0.3
            }
        },
        "roads": {
            "path": "http://localhost:8080/data/roads",
            "minZoom": 14,
            "style": {
                "fill-color": "rgba(0, 0, 0, 0.2)"
            }
        },
        "pavements": {
            "path": "http://localhost:8080/data/pavements",
            "minZoom": 14,
            "style": {
                "stroke-color": "rgba(0, 0, 0, 0.7)"
            }
        },
        "properties": {
            "path": "http://localhost:8080/data/properties",
            "minZoom": 15,
            "style": {
                "stroke-color": "black",
                "stroke-width": 0.3
            }
        },
        "trees": {
            "path": "http://localhost:8080/data/trees",
            "minZoom": 16,
            "style": {
                'circle-radius': 3,
                'circle-fill-color': "red",
            }
        },
        "greenAreas": {
            "path": "http://localhost:8080/data/greenAreas",
            "minZoom": 14,
            "style": {
                "fill-color": "rgba(0, 124, 0, 0.5)"
            }
        },
        "utilities": {
            "path": "http://localhost:8080/data/utilities",
            "minZoom": 15,
            "style": {
                "stroke-color": "black"
            }
        },
        "result": {
            "path": "http://localhost:8080/data/result",
            "minZoom": 12,
            "style": {
                "fill-color": "rgba(255, 255, 0, 0.9)"
            }
        }
    }
}