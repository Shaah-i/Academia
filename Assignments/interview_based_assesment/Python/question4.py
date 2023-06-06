"""This code is using pandas library to read a JSON file from a URL. It then drops some columns from the resulting dataframe, normalizes the geolocation column, drops the original geolocation column, converts the year column to a year format, and concatenates the resulting dataframes. Finally, it exports the resulting dataframe to a CSV file. This code is likely processing meteor data from NASA."""
import pandas as pd

URL=  'https://data.nasa.gov/resource/y77d-th95.json'


""" reads a JSON file from the URL provided and storing it as a pandas dataframe. The `orient='values'` parameter specifies that the JSON file is in a "values" orientation, meaning that the values in the JSON file are arranged in a list of lists format."""
df= pd.read_json(URL, orient='values')

## removing unnecessary columns
data = df.drop(['fall', ':@computed_region_cbhk_fwbd', ':@computed_region_nnqa_25f4'], axis=1)

## getting point cordinates from nested dictionary
point_coordinates= pd.json_normalize(df.geolocation)
data.drop(['geolocation'], axis=1, inplace=True)

## converting to datetime format
data['year']= pd.to_datetime(data['year'], format="%Y-%m-%dT%H:%M:%S.%f", errors = 'coerce').dt.year

## combining all dataframes
final_data= pd.concat([data,point_coordinates['coordinates']], axis= 1)

## renaming columns for bettre clarity
final_data.rename(columns={"coordinates": "point_coordinates"}, inplace= True)

## saving as a csv file
final_data.to_csv("metor_data.csv", index= False)