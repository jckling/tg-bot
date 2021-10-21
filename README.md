# tg-bot

使用 telegram bot 往频道内定时推送消息：
1. 每天早上 6:30 推送 Bing 壁纸
2. 每天晚上 22:00 推送百合会漫画更新
3. 每周六早上 7:45 推送 Pixiv 周榜

*注1：上面的时间是 Github Action 开始运行的时间，推送到频道内会有一定的延迟。*
*注2：百合会论坛内容按积分限制查看，这里并不能绕过*

## 说明

使用方式同 [jckling/Daily-Bonus](https://github.com/jckling/Daily-Bonus)，fork 本仓库设置 Secrets 就可以运行，自定义推送时间修改 .github/workflows/ 目录下对应的配置文件即可。

| Secret 名称            | 描述                   |
| --------------------- | --------------------- |
| TOKEN                 | telegram bot token    |
| CHAT_ID               | telegram channel name |
| PIXIV_REFRESH_TOKEN   | Pixiv refresh_token   |
| YAMIBO_COOKIES        | 百合会 Cookie           |

1. token 从 [@BotFather](https://telegram.me/botfather) 获取，chat_id 就是 `@bot`（假设频道链接为 https://t.me/bot）
2. Pixiv `refresh_token` 获取参见👉 [获取 Refresh Token](https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)
   - 如果使用 Chrome 可以从 [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads) 查看和下载对应版本的 chromedriver
3. 百合会论坛 `Cookie` 获取参见👉 [V2EX Cookie 查看](https://github.com/jckling/Daily-Bonus//#v2ex)

# 相关链接

- [Bots: An introduction for developers](https://core.telegram.org/bots)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [upbit/pixivpy](https://github.com/upbit/pixivpy)
