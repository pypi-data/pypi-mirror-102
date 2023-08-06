Wordpress-Search-Results-Scraper is a python library to search product on wordpress and get search results automatically using browser automation. 
It currently runs only on windows.

### Example1
In this example we first import library, then we search keyword and get search results.
```sh
from wordpress_search_results_scraper import *
wordpress.search(keyword='green')

response=wordpress.search_results()
search_results=response['body']

```

### Example2:- Get Search Results by loading themes 5 times
In this example we first import library, then we search keyword and get search results by loading themes 5 times.
```sh
from wordpress_search_results_scraper import *
wordpress.search(keyword='green')

for i in range(0,5):
	response=wordpress.search_results()
	search_results=response['body']
	wordpress.load_more_themes() #clicks on load more themes
```

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [bot_studio](https://pypi.org/project/bot_studio/)

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which search will be done.


### Installation

```sh
pip install wordpress-search-results-scraper
```

### Import
```sh
from wordpress_search_results_scraper import *
```

### Search keyword
```sh
wordpress.search(keyword='shoes')
```

### Get search results
```sh
response=wordpress.search_results()
search_results=response['body']
```

### Load more themes
```sh
wordpress.load_more_themes()
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

