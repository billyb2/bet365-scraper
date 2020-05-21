#Imports some stuff from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
#pyautogui allows me to click on the windows file prompt when it appears
import time
import sys

#Location of the chrome driver that allows selenium to work with it
driverpth = "chromedriver.exe"


options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#The location of the chrome binary
options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
#The user agent the browser is pretending to be
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://www.nj.bet365.com/#/IP/")
driver.add_cookie({'name': 'aps03', 'value': 'cf=N&cg=3&cst=0&ct=198&hd=N&lng=32&oty=2&tzi=2', 'sameSite': 'Lax'})

#The driver will wait up to 10 seconds for an element to appear on screen
driver.implicitly_wait(100)


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]").click()
driver.add_cookie({'name': 'aps03', 'value': 'cf=N&cg=3&cst=0&ct=198&hd=N&lng=32&oty=2&tzi=2', 'sameSite': 'Lax'})
driver.refresh()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
odds = soup.find_all('span', class_='ovm-ParticipantOddsOnly_Odds')
for odd in odds:
    print(odd.get_text())
