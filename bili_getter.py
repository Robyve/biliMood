import time
import requests
import pandas as pd

from tqdm import tqdm

import config
import header
import utils


aid = utils.bv2av(config.BILI_BV)
curr_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
outdir = f'./output/bili/bili_{curr_time_str}_{config.BILI_BV}.csv'
csv_header = ['作者', '内容', '时间', '点赞', '页码']


def get_comments(page_num):
    url = f'https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn={page_num}&type=1&oid={aid}&sort=2'
    try:
        res = requests.get(url, headers=header.BILI_HEADER)
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
    for page_num in tqdm(range(1, config.BILI_MAX_PAGE + 1)):
        success = get_comments(page_num)
        if not success:
            return


if __name__ == '__main__':
    main()
