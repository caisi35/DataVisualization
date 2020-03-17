import json
import codecs
from pyecharts import Tree


with codecs.open("../data/GDP_data.json",mode='r',encoding="utf-8") as f:
    j = json.load(f)
data = [j]
tree = Tree(title="World country GDP", width=1000, height=600, title_pos="center")
tree.add(name="First", data=data)
tree.render("TreeChart.html")