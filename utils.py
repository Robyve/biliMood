import codecs
import time
import requests

import config
import header


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
    headers = header.BILI_HEADER
    lst = codecs.decode(requests.get(url, headers=headers).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0:
        return "视频不存在！"
    return int(lst[16][1:-1])
