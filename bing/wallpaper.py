# -*- coding: utf-8 -*-
# @File     : wallpaper.py
# @Time     : 2021/04/16 13:49
# @Author   : Jckling

from datetime import datetime

import requests

BING_API = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
BING_URL = "https://cn.bing.com"


# 获取壁纸
def explore_wallpaper():
    r = requests.get(BING_API)

    # 图片地址
    obj = r.json()
    image = obj["images"][0]
    url = BING_URL + image["url"].split('&')[0]

    # 图片时间
    enddate = datetime.strptime(image["enddate"], "%Y%m%d")

    # 版权信息
    info = image["copyright"] + "\n" + url

    # 图片内容
    r = requests.get(url)

    return r.content, info
