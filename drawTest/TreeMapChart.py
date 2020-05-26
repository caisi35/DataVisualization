import json
from pyecharts import TreeMap


def tree_map():
    with open("../data/GDP_data_1.json", encoding="utf-8") as f:
        data_lzx = json.load(f)
    tree_map_lzx = TreeMap(title="2017年世界各个国家和地区的GDP-李兆旭", width=1000, height=600)
    tree_map_lzx.add(name="七大洲", data=data_lzx, is_label_show=True,
                     label_pos="inside", treemap_left_depth=1)
    tree_map_lzx.render("TreeMapChart.html")


if __name__ == '__main__':
    tree_map()
