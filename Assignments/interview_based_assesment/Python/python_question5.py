import requests
import pandas as pd
from datetime import datetime

## API link
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

## Send HTTP GET request to the API and fetch the data
response = requests.get(api_link)
data = response.json()

episodes= data["_embedded"]["episodes"]
df= pd.DataFrame()

for episode in episodes:
## Extract required attributes
    e_data = {
        "id": episode["id"],
        "url": episode["url"],
        "name": episode["name"],
        "season": episode["season"],
        "number": episode["number"],
        "type": episode["type"],
        "airdate": datetime.strptime(episode["airdate"], "%Y-%m-%d").date(),
        "airtime": datetime.strptime(episode["airtime"], "%H:%M").strftime("%I:%M %p"),
        "runtime": episode["runtime"],
        "average_rating": episode["rating"]["average"],
        "summary": episode["summary"],
        "medium_image_link": episode["image"]["medium"],
        "original_image_link": episode["image"]["original"]
        }
    df= df._append([e_data])

## Bringing data to desired form and resetting the index
df['summary'] = df['summary'].str[3:-4]
df.reset_index(drop=True, inplace=True)

## saving the dataframe to csv format
df.to_csv("TVshow_data.csv", index= False)
