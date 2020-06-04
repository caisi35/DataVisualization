from pyecharts import HeatMap, Map
import pandas as pd


def get_GDP_data(file_path):
    """

    :param file_path:
    :return:
    """
    # 加载数据，usecols：只使用的列名
    df = pd.read_csv(file_path, encoding='utf-8', usecols=['地区', '2017年'])
    province = []
    value = []
    for index, col in df.iterrows():
        # 切分地区名     有两个特殊的地区名为三个字
        if '黑龙' in col[0] or '内蒙' in col[0]:
            province.append(col[0][:3])
        else:
            province.append(col[0][:2])
        value.append(col[1])
    return province, value


def picture_map(province, value):
    map = Map('全国各地区2017年GDP统计——黄彩思', height=600)
    map.add('', province, value, is_visualmap=True, visual_range=[1200, 90000], is_label_show=True)
    map.render('2017GDP_map.html')


def get_AQI_data(file_path):
    df = pd.read_csv(file_path, encoding='utf-8', usecols=['Date', 'AQI'])
    data = []
    for index, col in df.iterrows():
        data.append([col[0],col[1]])

    return data


def picture_heatmap(data):
    hm = HeatMap('广州市2018年的空气质量指数日历热力图——黄彩思')
    # 参照https://www.jianshu.com/p/fc8c78e0df98
    hm.add('', data, is_calendar_heatmap=True,is_visualmap=True, calendar_date_range='2018',
           calendar_cell_size=['auto', 30], is_toolbox_show=False, visual_range=[10, 200],
           visual_split_number=5, is_piecewise=True, visual_orient="horizontal", visual_pos="center",)
    hm.render('hearmap_AQI.html')

if __name__ == '__main__':
    # file_GDP_path = '../data/全国各地区GDP统计.csv'
    # province, value = get_GDP_data(file_GDP_path)
    # picture_map(province, value)
    file_AQI_path = '../data/guangzhou_AQI_2018.csv'
    AQI_data = get_AQI_data(file_AQI_path)
    picture_heatmap(AQI_data)

