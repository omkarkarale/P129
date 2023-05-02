from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

star_table = soup.find_all('table', {"class":"wikitable sortable"})

dwarf_list= []

tr_tag = star_table[0].find_all('tr')

for tr in tr_tag:
    td_tag = tr.find_all('td')
    temp_list = []
    for td in td_tag:
        temp_list.append(td.text)
    dwarf_list.append(temp_list)

Name = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(dwarf_list)):
    Name.append(dwarf_list[i][0])
    Distance.append(dwarf_list[i][5])

    try:
        Mass.append(float(dwarf_list[i][8])*0.000954588)
    except:
        Mass.append(dwarf_list[i][8])

    try:
        Radius.append(float(dwarf_list[i][9])*0.102763)
    except:
        Radius.append(dwarf_list[i][9])

headers = ['Dwarf_Star_Name','Dwarf_Star_Distance','Dwarf_Star_Mass','Dwarf_Star_Radius'] 

df = pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=headers)

df.to_csv('dwarf_stars.csv', index=False)
