import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString

# Load the vector layer
gdf = gpd.read_file(r"C:\Local Development\projects\02 climathon2024\climathon2024\data\bratislava_osm.geojson")

# Check the structure and data types
print(gdf.info())

# Display the first few rows
print(gdf.head())

# Check for missing values
print(gdf.isnull().sum())

# Summary statistics for numeric columns
print(gdf.describe())

# Check the type of geometry in the GeoDataFrame
print(gdf.geom_type.value_counts())

# Check the Coordinate Reference System (CRS)
print(gdf.crs)

# Calculate the bounds of the geometries
print(gdf.total_bounds)
