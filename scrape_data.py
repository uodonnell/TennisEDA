import subprocess
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tqdm import tqdm

options = Options()
options.add_argument("--headless")

node_modules_bin = subprocess.run(
        ["npm", "bin"],
        stdout=subprocess.PIPE,
        universal_newlines=True,
        check=True
    )

node_modules_bin_path = node_modules_bin.stdout.strip()
chromedriver_path = Path(node_modules_bin_path) / "chromedriver"

browser = webdriver.Chrome(options=options, executable_path=str(chromedriver_path))

browser.get('https://www.atptour.com/en/rankings/singles')

data_file = open('tennis_player_data.csv', 'w')

data_file.write(
    'player' + ',' + 'career_length'+ ',' + 'backhand_type' + ',' +  'aces' + ',' + 'double_faults' + ',' + 'first_serve' + ',' + '1st_serve_points_won'
    + ',' + '2nd_serve_points_won' + ',' + 'break_points_faced' + ',' + 'break_points_saved' + ',' + 'service_games_played' + ',' +
    'service_games_won' + ',' + 'total_service_points_won' + ',' + '1st_serve_return_won' + ',' + '2nd_serve_return_won' + ',' +
    'total_break_pts' + ',' + 'break_pts_conv' + ','+ 'return_games_played' + ',' + 'return_games_won' + ','+
    'return_points_won' + ',' + 'total_pts_won' + ',' + '\n'
    )


for i in tqdm(range(1, 81)):

    #player = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="rankingDetailAjaxContainer"]/table/tbody/tr['+str(i)+']/td[4]/a')))
    # mine V 
    player = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH,  '//*[@id="player-rank-detail-ajax"]/tbody/tr['+str(i)+']/td[4]/span/a')))    
    print(player)                                                                         
    data_file.write(player.text + ',')       
 
    # click on the player's name to get to his page
    button1 = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[{i}]/td[4]/span/a')))
    browser.execute_script('arguments[0].click()', button1)                                                                                        
    turned_pro = WebDriverWait(browser, 40).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="playerProfileHero"]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/div[2]'))).text                                                                                        
    backhand = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="playerProfileHero"]/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/div/div[2]'))).text  
    backhand = backhand.split(',')[1]                                                                                         
    career_length = 2022 - int(turned_pro)
    data_file.write(str(career_length) + ',')
    data_file.write(str(backhand) + ',')

    # click on the "PLAYER STATS" button to navigate to page displaying match stats                        
    button2 = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div[3]/div/div[6]/a ')))
    browser.execute_script('arguments[0].click()', button2)
    WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="playerMatchFactsContainer"]')))
    # serving data for 1 player
    for y in range(1, 11):
        # get the table and each value
        player_serve_data = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="playerMatchFactsContainer"]/table[1]/tbody/tr['+str(y)+']/td[2]')))
        serve_data = player_serve_data.text.replace(',', '').replace('%', '')
        data_file.write(serve_data + ',')
    # return data for 1 player
    for z in range(1,9):
        player_return_data = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="playerMatchFactsContainer"]/table[2]/tbody/tr['+str(z)+']/td[2]')))
        return_data = player_return_data.text.replace(',', '').replace('%', '')
        data_file.write(return_data + ',')
    
    data_file.write('\n')
    browser.get('https://www.atptour.com/en/rankings/singles')

data_file.close()
