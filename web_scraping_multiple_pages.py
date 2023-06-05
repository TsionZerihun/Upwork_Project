import requests
import bs4 
import pandas as pd

baseurl = 'https://bscscan.com/dextracker'

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

page = page = requests.get(baseurl, headers = headers)
print(page.status_code)

header =[]
rows = []

for  x in range(1,60):
    page = requests.get(f'https://bscscan.com/dextracker?p={x}', headers=headers)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    
    table = soup.find('div', class_ = 'table-responsive mb-2 mb-md-0')
   

    for i, row in enumerate(table.find_all('tr')):
        if i==0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])




#baseurl = 'https://fastestlaps.com/tracks/adm-miachkovo'


'''for i in table.find_all('tr'):
    header = [el.text.strip() for el in i.find_all('th')]
'''
print(header)
data = pd.DataFrame(rows, columns=header)

data.to_csv('tabledata3.csv', index = False)
