Yellowpages-Search-Results-Scraper is a python library to search keyword on yellowpages and get search results automatically using browser automation. 
It currently runs only on windows.

### Example1
In this example we first import library, then we search keyword and get search results.
```sh
from yellowpages_search_results_scraper import *
yellowpages.search(keyword='hotels')

response=yellowpages.search_results()
search_results=response['body']

```

### Example2:- Get Search Results by loading data 5 times
In this example we first import library, then we search keyword and get search results.
```sh
from yellowpages_search_results_scraper import *
yellowpages.search(keyword='hotels')

for i in range(0,5):
	response=yellowpages.search_results()
	search_results=response['body']
	yellowpages.click_load_more() #clicks on load more
```

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [bot_studio](https://pypi.org/project/bot_studio/)

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which search will be done.


### Installation

```sh
pip install yellowpages-search-results-scraper
```

### Import
```sh
from yellowpages_search_results_scraper import *
```

### Search keyword
```sh
yellowpages.search(keyword='hotels')
```

### Get search results
```sh
response=yellowpages.search_results()
search_results=response['body']
```

### Load more data
```sh
yellowpages.click_load_more()
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

