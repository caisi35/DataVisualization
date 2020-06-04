import pandas as pd
from pyecharts import Radar, Boxplot


def nien_to_nan(df, columns):
    """
        将最大值的噪声数据设为nan
    :param df:      dataframe
    :param columns: 需要转的列
    :return:        新的dataframe
    """
    for column in columns:
        # 获取最大值
        max = df.loc[:, column].max()
        # 如果是未知噪声数据
        if max == 99 or max == 999 or max == 9999:
            # 获取存在噪声数据的所有行， 类型是一个dataframe
            birth_nien = df[df[column].isin([max])]
            # 遍历噪声数据行的index
            for index in birth_nien.index:
                # 将传入的dataframe中的噪声数据设为nan
                df.loc[index, column] = None
    return df


def get_data(file_path):
    """
    :param file_path:文件路径：str
    :return: tuple:存活婴儿、死亡婴儿中五个字段的平均值，类型为list
    """
    birth = pd.read_csv(file_path)
    # 使用loc 进行切片， 行：全选  列：选择不连续的用列表包含列名
    birth_nien = birth.loc[:, ['INFANT_ALIVE_AT_REPORT',
                               'MOTHER_AGE_YEARS',
                               'CIG_1_TRI',
                               'MOTHER_PRE_WEIGHT',
                               'OBSTETRIC_GESTATION_WEEKS',
                               'INFANT_WEIGHT_GRAMS']]

    birth_nien = nien_to_nan(birth_nien,
                             ['MOTHER_AGE_YEARS', 'CIG_1_TRI', 'MOTHER_PRE_WEIGHT', 'OBSTETRIC_GESTATION_WEEKS',
                              'INFANT_WEIGHT_GRAMS'])

    # birth_nien['INFANT_ALIVE_AT_REPORT'] == 'Y'   判断row的值：等于则为True  再使用DataFrame取为True的行
    y = birth_nien[birth_nien['INFANT_ALIVE_AT_REPORT'] == 'Y']
    n = birth_nien[birth_nien['INFANT_ALIVE_AT_REPORT'] == 'N']
    # 按列求平均值，跳过nan，
    # round(decimals=2)： 四舍五入取两位小数
    y_mean = list(y.mean(skipna=True, axis=0).round(decimals=2))
    n_mean = list(n.mean(skipna=True, axis=0).round(decimals=2))
    return y_mean, n_mean


def picture_radar(y_list, n_list):
    """
        绘制雷达图
    :param y_list: 存活婴儿的列平均值列表
    :param n_list: 死亡婴儿的列平均值列表

    """
    schema = [{'name': "母亲平均年龄", 'max': 40},
              {'name': "母亲平均吸烟数量", 'max': 1.2},
              {'name': "母亲平均体重", 'max': 200},
              {'name': "怀孕平均周数", 'max': 40},
              {'name': "婴儿平均体重", 'max': 3500}]
    radar = Radar('存活婴儿与死亡婴儿数据对比——雷达图（黄彩思）', height=500)
    radar.set_radar_component(c_schema=schema)
    radar.add('存活婴儿', [y_list], item_color='#2525f5',symbol=None, area_color='#2525f5', area_opacity=0.3,
              legend_top='bottom', line_width=3)
    radar.add('死亡婴儿', [n_list], item_color="#f9713c",symbol=None, area_color="#ea3a2e", area_opacity=0.3,
              legend_top='bottom', line_width=3, legend_text_size=20)
    radar.render('radar.html')


def picture_box(file_path):
    """
        绘制箱形图
    :param file_path:数据文件的路径
    """
    birth = pd.read_csv(file_path)
    birth_col = birth.loc[:, ['INFANT_ALIVE_AT_REPORT',
                              'BIRTH_YEAR',
                              'INFANT_WEIGHT_GRAMS']]
    # 取反，去除不需要的数据
    birth_nien = birth_col[~birth_col['INFANT_WEIGHT_GRAMS'].isin([9999])]
    # 按年分时间段
    year_2014 = birth_nien[birth_nien['BIRTH_YEAR'] == 2014]
    year_2015 = birth_nien[birth_nien['BIRTH_YEAR'] == 2015]
    # 再分每年中，存活与死亡的
    year_2014_y = year_2014[year_2014['INFANT_ALIVE_AT_REPORT'] == 'Y']
    year_2014_n = year_2014[year_2014['INFANT_ALIVE_AT_REPORT'] == 'N']
    year_2015_y = year_2015[year_2015['INFANT_ALIVE_AT_REPORT'] == 'Y']
    year_2015_n = year_2015[year_2015['INFANT_ALIVE_AT_REPORT'] == 'N']
    # 实例化一个箱形图对象
    box = Boxplot('存活婴儿与死亡婴儿数据对比——箱型图（黄彩思）')
    # 使用自带的prepare_data计算所需的五个数
    y_data = box.prepare_data([year_2014_y['INFANT_WEIGHT_GRAMS'],
                               year_2015_y['INFANT_WEIGHT_GRAMS']])
    n_data = box.prepare_data([year_2014_n['INFANT_WEIGHT_GRAMS'],
                               year_2015_n['INFANT_WEIGHT_GRAMS']])
    # 获取x_axis轴的数据：每个年度
    x_axis = birth_nien.drop_duplicates(subset='BIRTH_YEAR')['BIRTH_YEAR'].sort_values()

    box.add('存活婴儿', x_axis=x_axis, y_axis=y_data)
    box.add('死亡婴儿', x_axis=x_axis, y_axis=n_data, legend_pos='right')

    box.render('box.html')


if __name__ == '__main__':
    file_path = '../data/births_train.csv'
    y, n = get_data(file_path)
    picture_radar(y, n)
    picture_box(file_path)
