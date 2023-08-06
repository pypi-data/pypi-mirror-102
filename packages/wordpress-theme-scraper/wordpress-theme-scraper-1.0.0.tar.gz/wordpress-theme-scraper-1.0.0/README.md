Wordpress-Theme-Scraper is a python library to get theme information on wordpress automatically using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we will fetch the theme info.
```sh
from wordpress_theme_scraper import *
theme_url="https://wordpress.org/themes/twentytwentyone/"
response=wordpress.get_theme_info(theme_link=theme_url)
data=response['body']
```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which theme link will be opened.


### Installation

```sh
pip install wordpress-theme-scraper
```

### Import
```sh
from wordpress_theme_scraper import *
```

### Get theme info
```sh
response=wordpress.get_theme_info(theme_link='theme link')
data=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

