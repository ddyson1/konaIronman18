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
        name, _, swim, bike, run, div_rank, gender_rank, overall_rank = [col.text.strip() for col in row.find_all('td')[1:]]

        result[name].append({
            'div_rank': div_rank,
            'gender_rank': gender_rank,
            'overall_rank': overall_rank,
            'swim': swim,
            'bike': bike,
            'run': run,
        })

    return result

with open('data.txt', 'w') as txtfile:
    json.dump(parse_table(soup), txtfile)

print(json.dumps(parse_table(soup), indent=3))

'''

# print(soup.prettify())
# print(soup.title.string)
# print(soup.tr.text)
# print(soup.tbody)
# print(soup.find_all(re.compile("(td|div)")))

for link in soup.find_all('a'):
    print(link.get('href'))

'''
    
# Moving to the next page function

'''
counter = 1

while (counter <= 100):
    for post in posts:

        # Getting the title, author, ...
        # Writing to CSV and incre,enting counter...

    next_button = soup.find("span",class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(2)
    page = requests.get(((next_poage_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
''' 
