# -*- coding: utf-8 -*-
# @File     : cmd.py
# @Time     : 2021/04/29 17:34
# @Author   : Jckling

import argparse
import asyncio

from bilibili.updates import ups_updates
from bing.wallpaper import explore_wallpaper
from bot import bot, CHAT_ID
from pixiv.ranking import weekly_ranking
from yamibo.manga import yuri_manga

parser = argparse.ArgumentParser(description='Push message to telegram channel')
parser.add_argument('--daily', action='store_true', help='daily task, including bing_wallpaper')
parser.add_argument('--weekly', action='store_true', help='weekly task, including pixiv_illust_ranking')
parser.add_argument('--daily_night', action='store_true', help='daily night task, including yamibo_manga')

args = parser.parse_args()


async def main():
    try:
        if args.daily:
            # Bing 壁纸
            image, info = explore_wallpaper()
            await bot.sendPhoto(
                chat_id=CHAT_ID,
                photo=image,
                caption=info
            )

        if args.weekly:
            # Pixiv 插画周榜
            lst = weekly_ranking()
            await bot.sendMediaGroup(
                chat_id=CHAT_ID,
                media=lst
            )

        if args.daily_night:
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
    except Exception as e:
        print("Error: %s" % e)


asyncio.run(main())
