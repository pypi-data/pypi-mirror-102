Kmart-Product-Scraper is a python library to get product information on kmart automatically using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we will fetch the product info.
```sh
from kmart_product_scraper import *
product_url="https://www.kmart.com.au/product/santoku-knife/627809"
response=kmart.get_product_info(product_link=product_url)
data=response['body']
```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product link will be opened.


### Installation

```sh
pip install kmart-product-scraper
```

### Import
```sh
from kmart_product_scraper import *
```

### Get product info
```sh
response=kmart.get_product_info(product_link='product link')
data=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

