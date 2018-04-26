'''
Note:
for this program to run beautifulsoup4 and lxml are needed
if you don't have it installed on your computer, go to cmd and type:

    pip install beautifulsoup4
    pip install lxml

'''

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.tennis.com/rankings/WTA/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
ranking_table = soup.find('tbody')

ranking_table_rows = ranking_table.find_all('tr')

for tr in ranking_table_rows:
    td = tr.find_all('td')
    rows = []
    for i in td:
        rows.append(i.text)
    print(rows[0].strip() + " " + rows[2].strip().upper() +
          "\n\tPoints: " + rows[4].strip() + "\n")
