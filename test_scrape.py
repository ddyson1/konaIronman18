from bs4 import BeautifulSoup, Comment
from collections import defaultdict
import json
import requests
import re


sauce = 'http://m.ironman.com/triathlon/events/americas/ironman/world-championship/results.aspx'

r = requests.get(sauce)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

def parse_table(soup):
    result = defaultdict(list)
    my_table = soup.find('tbody')

    for node in my_table.children:
        if isinstance(node, Comment):
            # Get content and strip comment "<!--" and "-->"
            # Wrap the rows in "table" tags as well.
            data = '<table>{}</table>'.format(node[4:-3])
            break

        table = BeautifulSoup(data, 'html.parser')

        for row in table.find_all('tr'):
            name, country, div_rank, gender_rank, overall_rank, swim, bike, run, finish, points = [col.text.strip() for col in row.find_all('td')[1:]] 
                                            
            result[name].append({
                'country': country,
                'div_rank': div_rank,
                'gender_rank': gender_rank,
                'overall_rank': overall_rank,
                'swim': swim,
                'bike': bike,
                'run': run,
            })

        return result
    
print(json.dumps(parse_table(soup), indent=3))
