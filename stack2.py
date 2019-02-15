import requests
from pandas.io.json import json_normalize
import pandas as pd


request_url = 'http://m.ironman.com/Handlers/EventLiveResultsMobile.aspx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


page = ''
params = {
'year': '2018',
'race': 'worldchampionship',
'q': '',
'p': page,
'so': 'orank',
'sd': ''}

response = requests.get(request_url, headers=headers, params=params)
jsonObj = response.json()

lastPage = jsonObj['lastPage']

result = pd.DataFrame()
for page in range(1, lastPage):

    page = str(page)
    print ('Processed Page: '+ page)
    response = requests.get(request_url, headers=headers, params=params)
    jsonObj = response.json()

    temp_df = json_normalize(jsonObj['records'])
    result = result.append(temp_df)

result = result.reset_index(drop=True)
result.to_csv('stack2.csv', index=False)
