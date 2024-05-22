import geopandas as gpd

gdf = gpd.read_file(r"attachments\DM_20231020_125544.json")

gdf = gdf.to_crs(epsg=4326)
gdf["name"] = gdf["NAME_TC"] + " " + gdf["NAME"]

gdf.to_file("Hong_Kong_relic_map.geojson", driver="GeoJSON")

gdf["geometry"] = gdf["geometry"].centroid

gdf.to_file("Hong_Kong_relic_map_point.geojson", driver="GeoJSON")
