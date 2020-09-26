# Visualizing Policing in Chicago

#### Use Classification to predict if a crime will result in and arrest or no arrest and discover any meaningful takeaways from the variables and/or data.

##  Packages Used

pandas: Python package for data manipulation and analysis
numpy: fundamental package for scientific computing in Python
seaborn: Python visualization package based on matplotlib
pickle: Python module serializing and deserializing Python objects for faster object loading
sklearn: Python library built for machine learning; contains classification, regression, and clustering algorithms
Tableau: Visualization tool
Shapely: Python package for working with polygons and latitudinal and longitudinal dimensions

## Credit for Data:
Various datasets from Chicago Data Portal https://data.cityofchicago.org/
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2
https://data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information/x8fc-8rcq
https://data.cityofchicago.org/Health-Human-Services/Public-Health-Services-Chicago-Primary-Care-Commun/cjg8-dbka
https://data.cityofchicago.org/Community-Economic-Development/Grocery-Stores-2013/53t8-wyrc
https://data.cityofchicago.org/Health-Human-Services/Pharmacy-Status/2et2-5aw3
https://data.cityofchicago.org/Health-Human-Services/Chicago-Department-of-Public-Health-Clinic-Locatio/kcki-hnch
https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Locations-SY1920/tz49-n8ze
https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Progress-Reports-SY1/dw27-rash
https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
https://data.cityofchicago.org/Health-Human-Services/Food-Inspections-7-1-2018-Present/qizy-d2wf

Chicago Housing Metrics https://www.housingstudies.org/data-portal/


##  The project

Combine Chicago crime data from 2019 with community housing metrics and aggregated scores from the surrounding area around each crime. Scraped the chicago community metrics and wrote a function that relied on the Shapely package to build polygons of half-mile real world radius around each crime and aggregate all clinics, libraries, pharmacies, schools, grocery stores, and food inspection results done in said radius. Logistic Regression, Random Forest, and XGBoost models used for classification, Logistic Regression coefficients translated to percent impact on odds of arrest and interpreted. Tableau used to create tables and maps. Most interesting takeaway was the model suggesting that there is an inverse relationship between the community arrest percentage (arrest in community divided by total reported crime) and the community mortgage/foreclosure health (total community mortgage minus total community foreclosures divided by total community mortgages). All data was current for the 2019 calender year as to avoid partial year or covid concerns.

## Authors

Louis Sagan
