import pandas as pd
import numpy as np
from shapely.geometry import Point, Polygon


def get_radius(location):

    lat, long = location

    # Half Mile, in feet, converted to latitudinal change by approximating 101 ft per latitudinal second
    lat_buffer_length = .5 * 5280 / 101 / 3600
    # Half Mile, in feet, converted to longitudinal change by approximating 80 ft per longitudinal second
    long_buffer_length = .5 * 5280 / 80 / 3600
    # build a circle
    polygon_sides = 360

    angles = np.linspace(0, 2 * np.pi, polygon_sides, endpoint=False)
    points_list = [(lat + np.sin(a) * lat_buffer_length,
                        long + np.cos(a) * long_buffer_length)
                                       for a in angles]
    
    return Polygon(points_list)

def radius_metrics(polygon):

    schools = pd.read_pickle('schools.pkl')
    grocery_stores = pd.read_pickle('grocery_stores.pkl')
    clinics = pd.read_pickle('clinics.pkl')
    libraries = pd.read_pickle('libraries.pkl')
    pharmacies = pd.read_pickle('pharmacies.pkl')
    food_inspections = pd.read_pickle('food_inspections.pkl')

    # aggregating schools in radius 
    schools_in_radius = schools[schools['points'].apply(lambda x: x.within(polygon))]
    
    schools_in_radius.drop(['location', 'points', 'school_id', 'long_name', 'school_type', 'community_name']\
            , axis=1, inplace=True, errors='ignore')

    if len(schools_in_radius.index) == 0:
        schools_in_radius_metrics = np.zeros((1, len(schools_in_radius.columns))).reshape(1,-1)
    
    else:
        schools_in_radius_metrics = schools_in_radius.mean().values.reshape(1,-1)

    # aggregating grocery stores in radius
    grocery_stores_in_radius = grocery_stores[grocery_stores['points'].apply(lambda x: x.within(polygon))]

    grocery_stores_in_radius.drop(['location', 'points', 'store_name', 'community_name', 'community_number']\
        , axis=1, inplace=True, errors='ignore')
    
    if len(grocery_stores_in_radius.index) == 0:
        grocery_stores_in_radius_metrics = np.zeros((1, len(grocery_stores_in_radius.columns))).reshape(1,-1)
    
    else:
        grocery_stores_in_radius_metrics = grocery_stores_in_radius.mean().values.reshape(1,-1)

    # aggregating food inspecion results in radius
    food_inspections_in_radius = food_inspections[food_inspections['points'].apply(lambda x: x.within(polygon))]

    food_inspections_in_radius.drop(['location', 'points', 'community_name']\
        , axis=1, inplace=True, errors='ignore')

    if len(food_inspections_in_radius.index) == 0:
        food_inspections_in_radius_metrics = np.zeros((1, len(food_inspections_in_radius.columns))).reshape(1, -1)

    else:
        food_inspections_in_radius_metrics = food_inspections_in_radius.mean().values.reshape(1, -1)
    
    # count of clinics, libraries, pharmacies in radius
    clinics_count = 0
    libraries_count = 0
    pharmacies_count = 0
    
    clinics_in_radius = clinics[clinics['points'].apply(lambda x: x.within(polygon))]
    clinics_count = len(clinics_in_radius)

    libraries_in_radius = libraries[libraries['points'].apply(lambda x: x.within(polygon))]
    libraries_count = len(libraries_in_radius)

    pharmacies_in_radius = pharmacies[pharmacies['points'].apply(lambda x: x.within(polygon))]
    pharmacies_count = len(pharmacies_in_radius)

    facilities_count = np.array([clinics_count, libraries_count, pharmacies_count]).reshape(1,-1)
    
    return np.hstack((schools_in_radius_metrics, grocery_stores_in_radius_metrics, food_inspections_in_radius_metrics, facilities_count))
