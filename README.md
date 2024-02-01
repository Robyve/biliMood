# 社交平台评论爬虫

## 配置
- 如果失效，在`./cookies`中更换对应cookie

## 使用

#### Bilibili评论抓取
1. 将bilibili.com的cookie填入`config.py`下的`BLIL_COOKIE`。
   - 在bilibili.com登录你的b站账号，按`F12`，点击`网络`标签页，找到`www.bilibili.com`（如果没有就刷新一下网页），在右侧找到`Cookie:`项，复制即可。
   - cookie可能会失效，重新填入新cookie即可。
2. 找到你要爬取评论的视频，将视频BV号填入`config.py`下的`BLIL_BV`。
   - BV号可以视频网址中找到：` https://www.bilibili.com/video/BV*******/... `。
   - BV号无论是否包含开头的BV字母都可以使用。
3. 设置`config.py`下的`BLIL_MAX_PAGE`为你想抓取的评论总页数，也可以填一个很大的数来抓取所有评论，但此时进度条可能不会正常工作。
4. 运行bili_getter.py，抓取结果会以csv格式输出到`output/bili`下。

#### 情绪分析
1. 参照 https://blog.csdn.net/fuhao6363/article/details/128293350 取得APP_ID，API_KEY和SECRET_KEY。将它们填入`config.py`的对应位置。
2. 设置`config.py`下的`MOOD_IN_FILE`为要分析的csv文件