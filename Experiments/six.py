from pyecharts import HeatMap, Map
import pandas as pd


def picture_map(file_path_hcs):
    df_hcs = pd.read_csv(file_path_hcs, encoding='utf-8', usecols=['地区', '2017年'])
    province_hcs = []
    value_hcs = []
    for index_hcs, col_hcs in df_hcs.iterrows():
        # 切分地区名     有两个特殊的地区名为三个字
        if '黑龙' in col_hcs[0] or '内蒙' in col_hcs[0]:
            province_hcs.append(col_hcs[0][:3])
        else:
            province_hcs.append(col_hcs[0][:2])
        value_hcs.append(col_hcs[1])
    map_hcs = Map('全国各地区2017年GDP统计——黄彩思', height=600)
    map_hcs.add('', province_hcs, value_hcs, is_visualmap=True, visual_range=[1200, 90000], is_label_show=True)
    map_hcs.render('2017GDP_map.html')


def picture_heatmap(file_path_hcs):
    df_hcs = pd.read_csv(file_path_hcs, encoding='utf-8', usecols=['Date', 'AQI'])
    data_hcs = []
    for index_hcs, col_hcs in df_hcs.iterrows():
        data_hcs.append([col_hcs[0], col_hcs[1]])
    hm_hcs = HeatMap('广州市2018年的空气质量指数日历热力图——黄彩思')
    # 参照https://www.jianshu.com/p/fc8c78e0df98
    hm_hcs.add('', data_hcs, is_calendar_heatmap=True, is_visualmap=True, calendar_date_range='2018',
           calendar_cell_size=['auto', 30], is_toolbox_show=False, visual_range=[10, 200],
           visual_split_number=5, is_piecewise=True, visual_orient="horizontal", visual_pos="center", )
    hm_hcs.render('hearmap_AQI.html')


if __name__ == '__main__':
    file_GDP_path_hcs = '../data/national_provinces_GDP.csv'
    picture_map(file_GDP_path_hcs)
    file_AQI_path_hcs = '../data/guangzhou_AQI_2018.csv'
    picture_heatmap(file_AQI_path_hcs)
