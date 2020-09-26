import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import re

comm_map = pd.read_pickle('comm_map.pkl')

def get_community_name(location):

    location_in_chicago = Point(location)

    for index, row in comm_map.iterrows():

        chicago_community_polygon = Polygon(row['perim_lat_long_points'])
                                                
        if chicago_community_polygon.contains(location_in_chicago):
            
            return row['comm_name']

def chicago_lat_long_builder(series):

    match_list = re.findall(r'[-]?\d+\.\d+,?\s[-]?\d+\.\d+', series)
        
    lat_long = []

    for match in match_list:
        
        long, lat = sorted(match.replace(',', '').split())
        lat_long.append((float(lat), float(long)))

    if len(lat_long) > 1:                    
        return lat_long
    else:
        return lat_long[0]
