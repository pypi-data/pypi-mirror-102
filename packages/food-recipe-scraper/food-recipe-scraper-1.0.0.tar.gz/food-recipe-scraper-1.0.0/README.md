Food-recipe-Scraper is a python library to get recipe information on food.com automatically using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we will fetch the recipe info.
```sh
from food_recipe_scraper import *
recipe_url="https://www.food.com/recipe/creamy-cajun-chicken-pasta-39087"
response=food.get_recipe_info(recipe_link=recipe_url)
data=response['body']
```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which recipe link will be opened.


### Installation

```sh
pip install food-recipe-scraper
```

### Import
```sh
from food_recipe_scraper import *
```

### Get recipe info
```sh
response=food.get_recipe_info(recipe_link='recipe link')
data=response['body']
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

