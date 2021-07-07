"""
I need to:

1. Request GameStop news
2. Store all news in a sqlite database
3. If there is a new article, post it in r/Superstonk

"""

from bot.functions import check_update

if __name__ == "__main__":
    check_update()