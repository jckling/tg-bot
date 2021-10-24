# -*- coding: utf-8 -*-
# @File     : updates.py
# @Time     : 2021/10/24 16:09
# @Author   : Jckling


from datetime import datetime, timedelta

import requests

# 22:00 ~ 次日 22:00
today = datetime.now().replace(hour=22, minute=0, second=0)
yesterday = today - timedelta(days=1)

types = {
    0: "新动态",
    1: "转发动态",
    8: "新投稿",
    16: "短视频",
    64: "新专栏",
    256: "新音频"
}


# 从文件读取
def uid_lists(filename="./bilibili/uids.txt"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]


# 最新 12 条动态
def updates(uid):
    # need_top：1 带置顶, 0 不带置顶
    url = f"https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid={uid}&offset_dynamic_id=0&need_top=0"
    r = requests.get(url).json()
    template = ""
    for card in r['data']['cards']:
        # 发布时间
        timestamp = card['desc']['timestamp']
        time = datetime.utcfromtimestamp(timestamp) + timedelta(hours=8)
        if time > yesterday and time <= today:
            if template == "":
                # 个人信息
                uid = card['desc']['user_profile']['info']['uid']
                name = card['desc']['user_profile']['info'].get('uname')
                # 模板
                template = f"""
                🎇 <a href=https://space.bilibili.com/'{uid}'>{name}</a> 🎇
                """
            # 整合成列表
            template += format(card, time)
    return template


# 信息格式
def format(card, time):
    # 类型
    type = card['desc']['type']
    type = types.get(type, types[0])
    # 地址
    url = "https://t.bilibili.com/" + card['desc']['dynamic_id_str']
    # 模板
    template = f""" 📢 {time.time().strftime("%H:%M")} {type}：{url}
                """
    return template


# 获取 up 主动态
def ups_updates():
    message = """📢 <b>{date:%Y-%m-%d} Bilibili 动态</b>
        """.format(date=datetime.now())
    for uid in uid_lists():
        message += updates(uid)
    return message


if __name__ == '__main__':
    print(yesterday, today)
    msg = ups_updates()
    print(msg)
