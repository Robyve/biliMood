import codecs
from time import sleep

import pandas as pd
from aip import AipNlp
from tqdm import tqdm

APP_ID = '41653772'
API_KEY = 'I4vxnGp0o00NPFyOVDWNPuyI'
SECRET_KEY = 'F1QlH03WcPsR3Ss9Bx0g9Y83yx2COFsM'

indir = './output/bili/bili_2023-11-03-17-28-06_705162334.csv'
outdir = f'./output/bili/bili_2023-11-03-17-28-06_705162334_mood.csv'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_sentiments(text, i):
    try:
        sitems = client.sentimentClassify(text)['items'][0]  # 情感分析
        positive = sitems['positive_prob']  # 积极概率
        confidence = sitems['confidence']  # 置信度
        sentiment = sitems['sentiment']  # 0表示消极，1表示中性，2表示积极
        output = '{}\t{}\t{}\t{}\n'.format(i, positive, confidence, sentiment)
        f = codecs.open('sentiment.xls', 'a+', 'utf-8')
        f.write(output)
        f.close()
        print('Done')
    except Exception as e:
        print(e)


def main():
    df = pd.read_csv(indir)

    positive_prob_list = []
    confidence_list = []
    sentiment_list = []  # 最终判断：0表示消极，1表示中性，2表示积极

    commit_list = df['内容']
    for commit_text in tqdm(commit_list):
        print(commit_text)
        sitems = client.sentimentClassify(commit_text)
        while True:
            if 'items' in sitems.keys():
                break
            sleep(0.5)
            sitems = client.sentimentClassify(commit_text)
        sitems = sitems['items'][0]
        positive_prob_list.append(sitems['positive_prob'])
        print(positive_prob_list[-1], end='\t')
        confidence_list.append(sitems['confidence'])
        print(confidence_list[-1], end='\t')
        sentiment_list.append(sitems['sentiment'])
        print(sentiment_list[-1])

    df['积极概率'] = positive_prob_list
    df['置信度'] = confidence_list
    df['最终判断'] = sentiment_list
    csv_header = ['作者', '内容', '时间', '点赞', '页码', '积极概率', '置信度', '最终判断']
    df.to_csv(outdir, mode='a+', encoding='utf_8_sig', index=False, header=csv_header)


if __name__ == '__main__':
    main()
