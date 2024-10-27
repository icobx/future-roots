import requests
import json

# Define the Overpass API endpoint
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Define your Overpass query
query = """
[out:json];
(
  way["highway"](48.1482, 17.1067, 48.1734, 17.1740); // Get all highways
  way["cycleway"](48.1482, 17.1067, 48.1734, 17.1740); // Get all cycleways
);
out body;
>;
out skel qt;
"""

# Make the request to the Overpass API
response = requests.post(OVERPASS_URL, data={'data': query})
data = response.json()