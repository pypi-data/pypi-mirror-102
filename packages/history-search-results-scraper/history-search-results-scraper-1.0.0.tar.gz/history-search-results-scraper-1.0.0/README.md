History-Search-Results-Scraper is a python library to search keyword on history.com and get search results automatically using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we search keyword and get search results.
```sh
from history_search_results_scraper import *
history.search(keyword='war')

response=history.search_results()
search_results=response['body']

```

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [bot_studio](https://pypi.org/project/bot_studio/)

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which search will be done.


### Installation

```sh
pip install history-search-results-scraper
```

### Import
```sh
from history_search_results_scraper import *
```

### Search keyword
```sh
history.search(keyword='war')
```

### Get search results
```sh
response=history.search_results()
search_results=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

