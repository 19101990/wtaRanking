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
rows = []
for tr in ranking_table_rows:
    td = tr.find_all('td')
    for i in td:
        rows.append(i.text.strip()) # get rid of white spaces


# group each 5 items in the list in a new list
#(current position[0], previous position[1], name[2], country[3], points[4])
players = [rows[n:n+5] for n in range(0,len(rows), 5)]


# find player by ranking
def findPlayerByRanking():
    input_ranking = int(input("Enter ranking: "))
    if input_ranking == 0 or input_ranking > 200:
        print("Note: you can only search for players in range from 1 to 200")
    else:
        input_ranking-=1
        print(players[input_ranking][2])


# find player by country
def findPlayerByCountry():
    input_country = str(input("Enter country name: "))
    for player in players:
        if player[3] == input_country.title():
            print(player[2] + "(" + player[0] + ")")


# find player by name
def findPlayerByName():
    input_name = str(input("Enter player's name: "))
    for player in players:
        if player[2] == input_name.title():
            print("\t" + player[2].upper() +
                  "\n\tRanking: " + player[0] +
                  "\n\tPoints: " + player[4] +
                  "\n\tCountry: " + player[3])
            


print("====================================")
findPlayerByRanking()
print("====================================")
findPlayerByCountry()
print("====================================")
findPlayerByName()
print("====================================")
