import json
import codecs
from pyecharts import TreeMap


def tree_map():
    with open("../data/GDP_data_1.json", encoding="utf-8") as f:
        data = json.load(f)
    tree_map = TreeMap(title="World country GDP", width=1000,height=600)
    tree_map.add(name="First", data=data,is_label_show=True,
                 label_pos="inside",treemap_left_depth=1)
    return tree_map


if __name__ == '__main__':
    tree_map = tree_map()
    tree_map.render("TreeMapChart.html")