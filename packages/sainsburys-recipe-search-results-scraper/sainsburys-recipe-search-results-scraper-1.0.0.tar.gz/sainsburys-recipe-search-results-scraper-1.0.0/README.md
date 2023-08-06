Sainsburys-Recipe-Search-Results-Scraper is a python library to search keyword on sainsburys recipe and get search results automatically using browser automation. 
It currently runs only on windows.

### Example1
In this example we first import library, then we search keyword and get search results.
```sh
from sainsburys_recipe_search_results_scraper import *
sainsburys_recipe.search(keyword='pasta')

response=sainsburys_recipe.search_results()
search_results=response['body']

```

### Example2:- Get Search Results of first 5 pages
In this example we first import library, then we search keyword and get search results by loading data 5 times.
```sh
from sainsburys_recipe_search_results_scraper import *
sainsburys_recipe.search(keyword='pasta')

for i in range(0,5):
	response=sainsburys_recipe.search_results()
	search_results=response['body']
	sainsburys_recipe.click_next() #clicks on next page
```

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [bot_studio](https://pypi.org/project/bot_studio/)

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which search will be done.


### Installation

```sh
pip install sainsburys-recipe-search-results-scraper
```

### Import
```sh
from sainsburys_recipe_search_results_scraper import *
```

### Search keyword
```sh
sainsburys_recipe.search(keyword='pasta')
```

### Get search results
```sh
response=sainsburys_recipe.search_results()
search_results=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

