# 社交平台评论爬虫

## 配置

---
- 如果失效，在`./cookies`中更换对应cookie

## 使用

---
#### Bilibili
1. 将bilibili.com的cookie填入`config.py`下的`BLIL_COOKIE`。
   - 在bilibili.com登录你的b站账号，按`F12`，点击`网络`标签页，找到`www.bilibili.com`（如果没有就刷新一下网页），在右侧找到`Cookie:`项，复制即可。
   - cookie可能会失效，重新填入新cookie即可。
2. 找到你要爬取评论的视频，将视频BV号填入`config.py`下的`BLIL_BV`。
3. 运行bili_getter.py