import codecs
import time
import requests

import config


def trans_date(v_timestamp):
    """10位时间戳转换为时间字符串"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(v_timestamp))


def create_out_dict(header_list: list[str]):
    out_dict = {}
    for h in header_list:
        out_dict[h] = []
    return out_dict


def bv2av(bvid):
    url = "https://api.bilibili.com/x/web-interface/view?bvid=1vg4y1f7QU"
    headers = {
        'authority': 'api.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': config.BILI_COOKIE,
        'origin': 'https://www.bilibili.com',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }
    lst = codecs.decode(requests.get(url, headers=headers).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0:
        return "视频不存在！"
    return int(lst[16][1:-1])
