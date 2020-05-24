# Bet365-Scraper
This is a pretty simple Bet365 scraper using Selenium + Beautiful Soup. It can get the odds of any player from any currently running match

<b>Requirements:</b>
* beautifulsoup4
* selenium
* soupsieve
* urllib3

<p>While the latest versions of all of these should be compatible, using the versions listed in the req.txt file are guaranteed to work</p>

## Installation instructions
### For Windows
1. Install Chrome Beta using the install file in the repo
2. Install dependencies by running `pip install -r req.txt`
3. Include the get_data function by having `from scrape import *` in your program
4. Use the `get_data` function to retrieve data from any currently running game. Add True or False to whether to include debug info. to have certain commands print 