# -*- coding: utf-8 -*-
# @File     : bot.py
# @Time     : 2021/04/16 13:13
# @Author   : Jckling

import asyncio
import os

from bing.wallpaper import explore_wallpaper
from pixiv.ranking import weekly_ranking
from telegram import Bot
from yamibo.manga import yuri_manga

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# from telegram.utils import request
# proxy = request.Request(proxy_url='http://127.0.0.1:7890')
# bot = Bot(token=TOKEN, request=proxy)

bot = Bot(token=TOKEN)


async def main():
    # Bing 壁纸
    image, info = explore_wallpaper()
    await bot.sendPhoto(
        chat_id=CHAT_ID,
        photo=image,
        caption=info
    )

    # Pixiv 插画周榜
    lst = weekly_ranking()
    await bot.sendMediaGroup(
        chat_id=CHAT_ID,
        media=lst
    )

    # Yamibo 中文漫画更新
    msg = yuri_manga()
    await bot.sendMessage(
        chat_id=CHAT_ID,
        text=msg,
        parse_mode="HTML"
    )

    # Bilibili 动态更新
    msg = ups_updates()
    await bot.sendMessage(
        chat_id=CHAT_ID,
        text=msg,
        parse_mode="HTML",
        disable_web_page_preview=True
    )


if __name__ == '__main__':
    asyncio.run(main())
