import time
import requests
import pandas as pd

from tqdm import tqdm

import config
import utils


aid = utils.bv2av(config.BILI_BV)
MAX_PAGE = 4
curr_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
outdir = f'./output/bili/bili_{curr_time_str}_{aid}.csv'
csv_header = ['作者', '内容', '时间', '点赞', '页码']


def get_comments(page_num):
    url = f'https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn={page_num}&type=1&oid={aid}&sort=2'
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
    try:
        res = requests.get(url, headers=headers)
    except:
        return False
    data_list = res.json()['data']['replies']
    out_dict = utils.create_out_dict(csv_header)

    for item in data_list:
        out_dict['作者'].append(item['member']['uname'])
        out_dict['内容'].append(item['content']['message'])
        out_dict['时间'].append(utils.trans_date(item['ctime']))
        out_dict['点赞'].append(item['like'])
        out_dict['页码'].append(page_num)

    df = pd.DataFrame(out_dict)
    # 把评论数据保存到csv文件
    df.to_csv(outdir, mode='a+', encoding='utf_8_sig', index=False, header=False)
    return True


def main():
    out_dict = utils.create_out_dict(csv_header)
    df = pd.DataFrame(out_dict)
    df.to_csv(outdir, mode='a+', encoding='utf_8_sig', index=False, header=csv_header)
    for page_num in tqdm(range(1, MAX_PAGE + 1)):
        success = get_comments(page_num)
        if not success:
            return


if __name__ == '__main__':
    main()
