import pandas as pd
from pyecharts import Radar, Boxplot


def nien_to_nan(df, columns_hcs):
    """
        将最大值的噪声数据设为nan
    :param df:      dataframe
    :param columns_hcs: 需要转的列
    :return:        新的dataframe
    """
    for column_hcs in columns_hcs:
        # 获取最大值
        max_hcs = df.loc[:, column_hcs].max()
        # 如果是未知噪声数据
        if max_hcs == 99 or max_hcs == 999 or max_hcs == 9999:
            # 获取存在噪声数据的所有行， 类型是一个dataframe
            birth_nien_hcs = df[df[column_hcs].isin([max_hcs])]
            # 遍历噪声数据行的index
            for index_hcs in birth_nien_hcs.index:
                # 将传入的dataframe中的噪声数据设为nan
                df.loc[index_hcs, column_hcs] = None
    return df


def picture_radar(file_path):
    """
    :param file_path:文件路径：str
    """
    birth_hcs = pd.read_csv(file_path)
    # 使用loc 进行切片， 行：全选  列：选择不连续的用列表包含列名
    birth_nien_hcs = birth_hcs.loc[:, ['INFANT_ALIVE_AT_REPORT',
                               'MOTHER_AGE_YEARS',
                               'CIG_1_TRI',
                               'MOTHER_PRE_WEIGHT',
                               'OBSTETRIC_GESTATION_WEEKS',
                               'INFANT_WEIGHT_GRAMS']]

    birth_nien_hcs = nien_to_nan(birth_nien_hcs,
                             ['MOTHER_AGE_YEARS', 'CIG_1_TRI', 'MOTHER_PRE_WEIGHT', 'OBSTETRIC_GESTATION_WEEKS',
                              'INFANT_WEIGHT_GRAMS'])

    # birth_nien['INFANT_ALIVE_AT_REPORT'] == 'Y'   判断row的值：等于则为True  再使用DataFrame取为True的行
    y_hcs = birth_nien_hcs[birth_nien_hcs['INFANT_ALIVE_AT_REPORT'] == 'Y']
    n_hcs = birth_nien_hcs[birth_nien_hcs['INFANT_ALIVE_AT_REPORT'] == 'N']
    # 按列求平均值，跳过nan，
    # round(decimals=2)： 四舍五入取两位小数
    y_mean_hcs = list(y_hcs.mean(skipna=True, axis=0).round(decimals=2))
    n_mean_hcs = list(n_hcs.mean(skipna=True, axis=0).round(decimals=2))
    print('存活婴儿数据雷达图:', y_mean_hcs, '\n', '死亡婴儿数据雷达图:', n_mean_hcs)
    schema_hcs = [{'name': "母亲平均年龄", 'max': 40},
              {'name': "母亲平均吸烟数量", 'max': 1.2},
              {'name': "母亲平均体重", 'max': 200},
              {'name': "怀孕平均周数", 'max': 40},
              {'name': "婴儿平均体重", 'max': 3500}]
    radar_hcs = Radar('存活婴儿与死亡婴儿数据对比——雷达图(黄彩思)', height=500)
    radar_hcs.set_radar_component(c_schema=schema_hcs)
    radar_hcs.add('存活婴儿', [y_mean_hcs], item_color='#2525f5',symbol=None, area_color='#2525f5', area_opacity=0.3,
              legend_top='bottom', line_width=3)
    radar_hcs.add('死亡婴儿', [n_mean_hcs], item_color="#f9713c",symbol=None, area_color="#ea3a2e", area_opacity=0.3,
              legend_top='bottom', line_width=3, legend_text_size=20)
    radar_hcs.render('radar.html')


def picture_box(file_path):
    """
        绘制箱形图
    :param file_path:数据文件的路径
    """
    birth_hcs = pd.read_csv(file_path)
    birth_col_hcs = birth_hcs.loc[:, ['INFANT_ALIVE_AT_REPORT',
                              'BIRTH_YEAR',
                              'INFANT_WEIGHT_GRAMS']]
    # 取反，去除不需要的数据
    birth_nien_hcs = birth_col_hcs[~birth_col_hcs['INFANT_WEIGHT_GRAMS'].isin([9999])]
    # 按年分时间段
    year_2014_hcs = birth_nien_hcs[birth_nien_hcs['BIRTH_YEAR'] == 2014]
    year_2015_hcs = birth_nien_hcs[birth_nien_hcs['BIRTH_YEAR'] == 2015]
    # 再分每年中，存活与死亡的
    year_2014_y_hcs = year_2014_hcs[year_2014_hcs['INFANT_ALIVE_AT_REPORT'] == 'Y']
    year_2014_n_hcs = year_2014_hcs[year_2014_hcs['INFANT_ALIVE_AT_REPORT'] == 'N']
    year_2015_y_hcs = year_2015_hcs[year_2015_hcs['INFANT_ALIVE_AT_REPORT'] == 'Y']
    year_2015_n_hcs = year_2015_hcs[year_2015_hcs['INFANT_ALIVE_AT_REPORT'] == 'N']
    # 实例化一个箱形图对象
    box_hcs = Boxplot('存活婴儿与死亡婴儿体重对比——箱型图(黄彩思)')
    # 使用自带的prepare_data计算所需的五个数
    y_data_hcs = box_hcs.prepare_data([year_2014_y_hcs['INFANT_WEIGHT_GRAMS'],
                               year_2015_y_hcs['INFANT_WEIGHT_GRAMS']])
    n_data_hcs = box_hcs.prepare_data([year_2014_n_hcs['INFANT_WEIGHT_GRAMS'],
                               year_2015_n_hcs['INFANT_WEIGHT_GRAMS']])
    # 获取x_axis轴的数据：每个年度
    x_axis_hcs = birth_nien_hcs.drop_duplicates(subset='BIRTH_YEAR')['BIRTH_YEAR'].sort_values()
    print('存活婴儿数据箱型图:', y_data_hcs, '\n', '死亡婴儿数据箱型图:', n_data_hcs)
    box_hcs.add('存活婴儿', x_axis=x_axis_hcs, y_axis=y_data_hcs)
    box_hcs.add('死亡婴儿', x_axis=x_axis_hcs, y_axis=n_data_hcs, legend_pos='right')

    box_hcs.render('box.html')


if __name__ == '__main__':
    file_path = '../data/births_train.csv'
    picture_radar(file_path)
    picture_box(file_path)
