from pyecharts import WordCloud
from jieba.analyse import extract_tags
import jieba
import pandas as pd


def get_text():
    # 加载文件
    data = pd.read_excel('../data/internship_consumption.xlsx', header=None, keep_default_na='')
    str = ''
    # 遍历获取没行数据
    for index, row in data.iterrows():
        if row[5] and index != 0:
            # print(index, row[5])
            # 将每行数据进行拼接
            str = str + row[5] + ' '
    return str


def content_key(text):
    resutl = extract_tags(sentence=text,topK=50, withWeight=True)
    attr = []
    value = []
    for i, j in resutl:
        attr.append(i)
        value.append(j)
    wordcloud = WordCloud('关键字提取结果(top50)', height=600)
    wordcloud.add('', attr, value, shape='star')
    wordcloud.render('key.html')


def word_count(text):
    words = jieba.cut(text)
    word_list = list(word for word in words)
    df = pd.DataFrame(word_list, columns=['word'])
    result = df.groupby(['word']).size().sort_values(ascending=False)
    words = []
    count = []
    for i in range(0,50):
        if result.index[i] in ',.!?，。！？~`、/;；：‘’“”()（）':
            continue
        else:
            words.append(result.index[i])
            count.append(result[i])
    wordcloud = WordCloud('词频统计结果(top50)', height=600)
    wordcloud.add('', words, count, shape='star')
    wordcloud.render()


if __name__ == '__main__':
    str = get_text()
    word_count(text=str)
    content_key(str)
