import requests
import bs4
import pandas as pd
from lxml import html

import urllib.request


# make a request from a webpage
url = 'https://bscscan.com/dextracker'
result = requests.get(url)

#to make sure the websiite is accessible; 200 ok response
print(result.status_code)

# to check the HTTP header
print(result.headers)

#to bypass the 403 forbidden msg 
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

res1 = requests.get(url, headers= headers)
print(res1.status_code)

# comparing it with a normal web site
url2 = 'https://fastestlaps.com/tracks/adm-miachkovo'
res2 = requests.get(url2)
print(res2.status_code)
#print(res2)

# extract the data from the web and store it on variable
soup = bs4.BeautifulSoup(result.text, 'html.parser')
soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
soup1 = bs4.BeautifulSoup(res1.content, 'html.parser')
#print(soup1)
#print(soup1.prettify())

# First get the div or table object for web scraping
table = soup1.find('div', class_ = 'table-responsive mb-2 mb-md-0')


# then iterate over each values of table rows

header = []
rows = []

for i, row in enumerate(table.find_all('tr')):
    if i==0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)

#getting the dataframe using pandas

data = pd.DataFrame(rows, columns=header)
#print(data)


# Exporting the data into excel
data.to_csv('tabledata1.csv', index = False)



#new reading of the site
#with urllib.request.urlopen('https://bscscan.com/dextracker') as response:
#    source = response.read()
#print(source)



#get the div tag/ but in our case we want the table so get table tag
t1 = soup1.find_all('div', class_ = 'card-body')
t2 = soup.find_all('div', class_ = 'table-responsive mb-2 mb-md-0')
t3 = soup.find_all('table',class_ = 'table table-hover')
t4 = soup.find_all('thead', class_ = 'thead-light')
#List to store the data
data = []
'''
for i in t4:
    span = i.find('th')
    data.append(span.string)
print(data)    

print('Classes of each table:')
for table in soup.find_all('div'):
    print(table.get('class'))    '''
