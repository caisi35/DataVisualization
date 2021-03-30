from pyecharts import WordCloud
from jieba.analyse import extract_tags
import jieba
from docx import Document
import pandas as pd

def get_data():
    document = Document('../data/To_XiaoMei.docx')
    text = ''
    for p in document.paragraphs:
        # print(p.text)
        text = text + p.text + ' '
    return text


def word_count(text):
    words = jieba.cut(text)
    word_list = list(word for word in words)
    df = pd.DataFrame(word_list, columns=['word'])
    result = df.groupby(['word']).size().sort_values(ascending=False)
    words = []
    count = []
    for i in range(0, 50):
        if result.index[i] in ',.!?，。！？~`、/;；：‘’“”()（）':
            continue
        else:
            words.append(result.index[i])
            count.append(result[i])
    wordcloud = WordCloud('词频统计结果(top50)', height=600)
    wordcloud.add('', words, count, shape='star')
    wordcloud.render()


def content_key(text):
    resutl = extract_tags(sentence=text, topK=50, withWeight=True)
    attr = []
    value = []
    for i, j in resutl:
        attr.append(i)
        value.append(j)
    wordcloud = WordCloud('关键字提取结果(top50)', height=600)
    wordcloud.add('', attr, value, shape='star')
    wordcloud.render('key.html')


if __name__ == '__main__':
    text = get_data()
    # print(text)
    content_key(text)
    word_count(text)
