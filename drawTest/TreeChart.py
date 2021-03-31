import json
import codecs
from pyecharts import Tree


def tree_chart():
    with codecs.open("../data/GDP_data.json",mode='r',encoding="utf-8") as f:
        j = json.load(f)
    data = [j]
    tree = Tree(title="World country GDP", width=1000, height=600, title_pos="center")
    tree.add(name="First", data=data)
    return tree


if __name__ == '__main__':
    tree = tree_chart()
    tree.render("TreeChart.html")