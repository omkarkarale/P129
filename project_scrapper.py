from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

table = soup.find_all('table', {'class':"wikitable sortable"})

star_data = []

tr_tag = table[0].find_all('tr')

for tr in tr_tag:
    temp_list = []
    for td in tr.find_all('td'):
        temp_list.append(td.text.strip())
    star_data.append(temp_list)

Name = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(star_data)):
    Name.append(star_data[i][1])
    Distance.append(star_data[i][3])
    Mass.append(star_data[i][5])
    Radius.append(star_data[i][6])

headers = ['Brightest_Star_Name', 'Brightest_Star_Distance', 'Brightest_Star_Mass', 'Brightest_Star_Radius']

df = pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=headers)

df.to_csv('brightest_stars.csv', index=False)

