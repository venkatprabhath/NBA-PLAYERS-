
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nba_players_list_url = 'https://www.nba.com/players'
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm- usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_names(driver):
   player_name_tag = 'tr'
   driver.get(nba_players_list_url)
   names = driver.find_elements(By.TAG_NAME,player_name_tag )
   return names

def full_history(driver):
  names = driver.find_elements(By.TAG_NAME,'tr' )
  for name in names:
    player_history= name.text
    player_status = player_history.split()

  b = full_history(driver)
  nba_players_list_url = 'https://www.nba.com/players'
  driver = get_driver()
  driver.get(nba_players_list_url)
  x= []
  x.append(b)
  return x  
  
  #return{

#def data(driver):
  
    

if __name__== "__main__" :
  #nba_players_list_url = 'https://www.nba.com/players'
  driver = get_driver()
  driver.get(nba_players_list_url)
  
  print(full_history(driver))

  #print('get the player names')
  #names = get_names(driver)
  


  #print('parsing 51 rows')


    
    
  





  

