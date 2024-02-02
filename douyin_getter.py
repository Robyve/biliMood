import time
import requests
import pandas as pd

from tqdm import tqdm

import config
import utils

video_id = config.DOUYIN_VIDEO_ID
curr_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
outdir = f'./output/douyin/douyin_{curr_time_str}.csv'
csv_header = ['作者', '内容', '时间', '点赞', '页码']


def get_comments(page_num):
    url = f'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&' \
          f'aid=6383&channel=channel_pc_web&' \
          f'aweme_id={video_id}&' \
          f'cursor={(page_num - 1) * 50}&' \
          f'count=50&item_type=0&' \
          f'rcFT=&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&' \
          f'browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=99.0.4844.51&' \
          f'browser_online=true&engine_name=Blink&engine_version=99.0.4844.51&os_name=Windows&os_version=10&' \
          f'cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=0&' \
          f'webid=7082249047388145183&msToken=QWSrXp1LBsAJx5ebu3Xk7Ngwx3nHhQVsOCDXXYdq3e_pA-zZ9fJQjIUvVtcXRt1QsuhdrP-F47kapoadK_ZlMkYZbtgFHK6gO7Yvg5_FOLbVyvxugb_Azp-WjXGZ4w9q&X-Bogus=DFSzswVL9c0ANr98SlqafGUClL9E&_signature=_02B4Z6wo00001OaWiIgAAIDBzRzTTsCKJKzmlowAAFvuTAqjP5WE9ZlERwOQJsQRqw5IfPL3OR3ay.tAxct-hAEFfBTSSxfJPx4JOtmjEkqpbIbXVBKVk9.Q5JXAJ9XdKE.-VfGi5xy9Lrxg23'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'cookie': config.DOUYIN_COOKIE,
        'Referer': f'https://www.douyin.com/video/{video_id}',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
    try:
        res = requests.get(url, headers=headers)
    except:
        return False
    data_list = res.json()['comments']
    out_dict = utils.create_out_dict(csv_header)
    for item in data_list:
        out_dict['作者'].append(item['user']['nickname'])
        out_dict['内容'].append(item['text'])
        out_dict['时间'].append(utils.trans_date(item['create_time']))
        out_dict['点赞'].append(item['digg_count'])
        out_dict['页码'].append(page_num)
    df = pd.DataFrame(out_dict)
    # 把评论数据保存到csv文件
    df.to_csv(outdir, mode='a+', encoding='utf_8_sig', index=False, header=False)
    return True


def main():
    out_dict = utils.create_out_dict(csv_header)
    df = pd.DataFrame(out_dict)
    df.to_csv(outdir, mode='a+', encoding='utf_8_sig', index=False, header=csv_header)

    for page_num in tqdm(range(1, config.DOUYIN_MAX_PAGE + 1)):
        success = get_comments(page_num)
        if not success:
            return


if __name__ == '__main__':
    main()
