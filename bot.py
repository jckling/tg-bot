# -*- coding: utf-8 -*-
# @File     : test.py
# @Time     : 2021/04/16 13:13
# @Author   : Jckling

import os

from telegram import Bot

from bing.wallpaper import explore_wallpaper
from pixiv.ranking import weekly_ranking

TOKEN = os.environ.get("TOKEN") or "1785476933:AAGqa5bLb--JULW1RzEUMm5fvTUYGVhkqZw"
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

if __name__ == '__main__':
    # Bing 壁纸
    image, info = explore_wallpaper()
    bot.sendPhoto(
        chat_id=CHAT_ID,
        photo=image,
        caption=info
    )

    # Pixiv 插画周榜
    lst = weekly_ranking()
    bot.sendMediaGroup(
        chat_id=CHAT_ID,
        media=lst
    )
