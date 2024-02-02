# Social Media Comment Scraper

## Setup
Run the following command to set up the environment:
```shell
pip install -r requirements.txt
```
## Usage

### Bilibili Comment Scraping
1. Enter your bilibili.com cookie into `BLIL_COOKIE` in `config.py`.
   - Log into your account on bilibili.com, press `F12`, click the `Network` tab, find `www.bilibili.com` (refresh the page if it's not there), find the `Cookie:` field on the right side, and copy it.
   - The cookie might expire, in which case simply enter a new cookie.
2. Find the video from which you want to scrape comments, and enter its BV number into `BLIL_BV` in `config.py`.
   - The BV number can be found in the video URL: `https://www.bilibili.com/video/BV*******/...`.
   - The BV number can be used with or without the leading BV letters.
3. Set `BLIL_MAX_PAGE` in `config.py` to the total number of comment pages you want to scrape, or enter a very large number to scrape all comments, but the progress bar may not work properly in this case.
4. Run `bili_getter.py`, the scraping result will be output in csv format under `output/bili`.

### Douyin Comment Scraping
1. Enter your douyin.com cookie into `DOUYIN_COOKIE` in `config.py`.
   - Log into your account on douyin.com, press `F12`, click the `Network` tab, find `www.douyin.com` (refresh the page if it's not there), find the `Cookie:` field on the right side, and copy it.
   - The cookie might expire, in which case simply enter a new cookie.
2. Find the video from which you want to scrape comments, and enter its ID into `DOUYIN_VIDEO_ID` in `config.py`.
   - The Douyin video ID can be found in the **details page** URL: `https://www.douyin.com/video/*******`.
   - The video ID is not visible when browsing videos on the homepage, right-click and click `video details page` to navigate the details page.
3. Set `DOUYIN_MAX_PAGE` in `config.py` to the total number of comment pages you want to scrape, or enter a very large number to scrape all comments, but the progress bar may not work properly in this case.
4. Run `douyin_getter.py`, the scraping result will be output in csv format under `output/douyin`.

### Sentiment Analysis
1. Sentiment analysis is based on the sentiment analysis function of the natural language processing model from Baidu AI Open Platform. Refer to https://blog.csdn.net/fuhao6363/article/details/128293350 to get the APP_ID, API_KEY, and SECRET_KEY. Enter them into their respective places in `config.py`.
2. Set `MOOD_IN_FILE` in `config.py` to the csv file you want to analyze.
3. Run `mood.py`, the analysis result will be output under `output/mood`, with the original file name plus a _mood suffix.
