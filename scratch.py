import requests
from bs4 import BeautifulSoup

nba_players_list_url = 'https://www.nba.com/players'
response = requests.get(nba_players_list_url)

print('status code', response.status_code)
print('out put', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('page title ', doc.title.text)

# find all the video divs

videos_divs = doc.find_all('tr')
print(f'Found  {len(videos_divs)} videos')
videos_div= videos_divs[0]
player_name = videos_div.find_all('a', class_= 't6')
print(player_name)
