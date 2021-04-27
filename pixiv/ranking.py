# -*- coding: utf-8 -*-
# @File     : charts.py
# @Time     : 2021/04/27 17:39
# @Author   : Jckling

from pixivpy3 import AppPixivAPI
from telegram import InputMediaPhoto
import os

USERNAME = os.environ.get("PIXIV_USERNAME")
PASSWORD = os.environ.get("PIXIV_PASSWORD")
REFRESH_TOKEN = os.environ.get("PIXIV_REFRESH_TOKEN")

tabs = ["综合", "插画", "动图", "漫画", "小说"]


def download_images():
    # 登录
    api = AppPixivAPI()
    api.auth(refresh_token=REFRESH_TOKEN)

    # 图像列表
    lst = []

    # [day, week, month, day_male, day_female, week_original, week_rookie, day_manga]
    json_result = api.illust_ranking('week')
    for illust in json_result.illusts:
        # 下载图片
        api.download(illust.image_urls.medium, fname=open('illust_%s.jpg' % (illust.id), 'wb'))

        # 打开图片
        f = open('illust_%s.jpg' % (illust.id), 'rb')
        info = "{} ({})\n{}({})".format(illust.title, illust.id, illust.user.name, illust.user.id)
        photo = InputMediaPhoto(media=f,
                                caption=info)
        lst.append(photo)

        # 打印信息
        print("[%s] \t%s\t\n" % (illust.title, illust.image_urls.medium), end="")

    return lst


def weekly_ranking():
    return download_images()


if __name__ == '__main__':
    lst = weekly_ranking()
    print(lst)
