
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

nba_players_list_url = 'https://www.nba.com/players'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)




driver.get(nba_players_list_url)

print('page title', driver.title)




