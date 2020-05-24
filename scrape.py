# Imports some stuff from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from bs4 import BeautifulSoup


# Location of the chrome driver that allows selenium to work with it
driverpth = "chromedriver.exe"

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
# The location of the chrome binary
options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
# The user agent the browser is pretending to be
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/74.0.3729.169 Safari/537.36')
driver = webdriver.Chrome(executable_path=driverpth, options=options)
driver.get("https://www.nj.bet365.com/#/IP/")

# The driver will wait up to 30 seconds for an element to appear on screen
driver.implicitly_wait(30)
driver.add_cookie({'name': 'aps03', 'value': 'cf=N&cg=3&cst=0&ct=198&hd=N&lng=32&oty=2&tzi=2', 'sameSite': 'Lax'})


def get_data(game, debug):
    driver.add_cookie({'name': 'aps03', 'value': 'cf=N&cg=3&cst=0&ct=198&hd=N&lng=32&oty=2&tzi=2', 'sameSite': 'Lax'})
    driver.refresh()
    driver.add_cookie({'name': 'aps03', 'value': 'cf=N&cg=3&cst=0&ct=198&hd=N&lng=32&oty=2&tzi=2', 'sameSite': 'Lax'})

    if debug:
        print('Getting ' + game + ' data...')

        try:
            driver.refresh()
            driver.find_element_by_xpath("//div[text()=\'" + game + "\']").click()
            print('Waiting for page to load...')
            driver.find_element_by_class_name("ovm-ParticipantOddsOnly_Odds")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            players = soup.find_all('div', class_='ovm-FixtureDetailsWithIndicators_Team')
            odds = soup.find_all('span', class_='ovm-ParticipantOddsOnly_Odds')

            data = {}

            for i in range(len(odds)):
                data[players[i].get_text()] = odds[i].get_text()

            return data

        except NoSuchElementException:
            print("ERROR! No " + game + " games currently running!")
            return None

        except InvalidCookieDomainException:
            print("ERROR! Can't load bet365")
            return None

        except:
            print("Something went wrong, though I don't know what!")
            return None

    else:
        try:
            driver.refresh()
            driver.find_element_by_xpath("//div[text()=\'" + game + "\']").click()
            driver.find_element_by_class_name("ovm-ParticipantOddsOnly_Odds")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            players = soup.find_all('div', class_='ovm-FixtureDetailsWithIndicators_Team')
            odds = soup.find_all('span', class_='ovm-ParticipantOddsOnly_Odds')

            data = {}

            for i in range(len(odds)):
                data[players[i].get_text()] = odds[i].get_text()

            return data

        except:
            return None
