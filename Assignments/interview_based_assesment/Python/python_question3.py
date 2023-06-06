"""This code is using pandas library to read a JSON file from a URL. It then normalizes the data and saves it as an Excel file named "pokemon_data.xlsx". Specifically, it is reading a JSON file containing information about Pokemon from the game Pokemon Go and extracting the data into a structured format using pandas."""

import pandas as pd

URL=  'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

""" reads a JSON file from the URL provided and storing it as a pandas dataframe. The `orient='values'` parameter specifies that the JSON file is in a "values" orientation, meaning that the values in the JSON file are arranged in a list of lists format."""
df= pd.read_json(URL, orient='values')

## getting all data from nested dictionary
data= pd.json_normalize(df['pokemon'], max_level=1)

## there is a column named "num" whic is redundunt and not there in final desired data attributes. So removing it.
data.drop("num", axis= 1, inplace= True)

## saving as a excel file
data.to_excel("pokemon_data.xlsx")