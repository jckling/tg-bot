# -*- coding: utf-8 -*-
# @File     : manga.py
# @Time     : 2021/04/30 10:48
# @Author   : Jckling

import os
from collections import namedtuple
from datetime import datetime, timedelta

import requests
from lxml import html

# cookies
COOKIES = os.environ.get("YAMIBO_COOKIES")
SESSION = requests.Session()

HEADERS = {
    "Host": "bbs.yamibo.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "sec-ch-ua-mobile": "?0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://bbs.yamibo.com/forum-13-1.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,da;q=0.5",
    "Cookie": COOKIES
}


# 中文百合漫画区
def yuri_manga():
    Manga = namedtuple('Manga', ['title', 'link', 'time'])
    Manga_List = []
    for i in range(1, 5):
        url = "https://bbs.yamibo.com/forum-30-{}.html"
        r = SESSION.get(url.format(i), headers=HEADERS)

        tree = html.fromstring(r.text)
        threads = tree.xpath('//tbody[starts-with(@id, "normalthread")]/tr')
        for thread in threads:
            # 标题
            title = thread.find('th[@class="common"]')
            if title is None:
                title = thread.find('th[@class="new"]')
            title = title.find('a[@class="s xst"]')

            # 网址
            link = "https://bbs.yamibo.com/" + title.get("href")

            # 发布时间
            time = thread.find('td[@class="by"]/em/span')
            post_time = datetime.strptime(time.text, "%Y-%m-%d %H:%M")
            today = datetime.now()
            yesterday = today.date() - timedelta(days=1)
            if post_time.date() == today.date() or \
                    (post_time.date() == yesterday and post_time.time() > today.time()):
                Manga_List.append(Manga(title.text, link, post_time))
        else:
            if post_time.date() != datetime.now().date():
                break

    # 整合成列表
    template = """✨ <a href='{link}'>{title}</a>

"""
    message = """📢 <b>{date:%Y-%m-%d} <a href='https://bbs.yamibo.com/forum-30-1.html'>中文百合漫画</a></b>

""".format(date=datetime.now())
    for manga in Manga_List:
        message += template.format(title=manga.title, link=manga.link)

    return message


if __name__ == '__main__':
    msg = yuri_manga()
    print(msg)
