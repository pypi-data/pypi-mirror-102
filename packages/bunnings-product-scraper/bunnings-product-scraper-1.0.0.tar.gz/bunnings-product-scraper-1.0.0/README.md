Bunnings-Product-Scraper is a python library to get product information on bunnings automatically using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we will fetch the product info.
```sh
from bunnings_product_scraper import *
product_url="https://www.bunnings.com.au/riva-395-914-x-914-1214mm-roman-chain-light-filtering-tuscany-blind_p1284545"
response=bunnings.get_product_info(product_link=product_url)
data=response['body']
```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product link will be opened.


### Installation

```sh
pip install bunnings-product-scraper
```

### Import
```sh
from bunnings_product_scraper import *
```

### Get product info
```sh
response=bunnings.get_product_info(product_link='product link')
data=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

