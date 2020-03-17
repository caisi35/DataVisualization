import json
import codecs
from pyecharts import TreeMap


with open("../data/GDP_data_1.json", encoding="utf-8") as f:
    data = json.load(f)
tree_map = TreeMap(title="World country GDP", width=1000,height=600)
tree_map.add(name="First", data=data,is_label_show=True,
             label_pos="inside",treemap_left_depth=1)
tree_map.render("TreeMapChart.html")