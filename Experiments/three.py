import pandas as  pd
from itertools import groupby
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
# 直接读取1960年的列
birth_rate = pd.read_csv('../data/birth-rate.csv')['1960']
# 去除空值
birth_rate.dropna(inplace=True)
last_data = birth_rate
# 保留一位小数
birth_rate = list(round(birth_rate, 1))
# 排序
birth_rate.sort()
data_dic = {}
# 数据处理
for k, g in groupby(birth_rate,key= lambda x:int(x)):
    # 取小数
    g_list = map(lambda y:divmod(int(y*10), 10)[1], list(g))
    # 转为列表
    g_list = list(g_list)
    # 如果为偶数，则加入到前面的奇数列表中
    if k % 2 ==0:
        # 25没有数据会有异常
        try:
            data_dic[k-1] = data_dic[k-1] + g_list
        except KeyError as e:
            data_dic[int(str(e))]=g_list
    # 如果为奇数插入字典
    else:
        data_dic[k] = g_list
# 格式化输出成茎叶图
print('黄彩思1704010135')
# 遍历字典
x = []
for k,v in data_dic.items():
    a = ''
    # 循环输出列表数据并拼接成字符串
    for i in v:
        a = a + ' ' + str(i)
    # 格式化输出
    # print(str(k).rjust(5), a)
    x.append(k)
x.append(57)

plt.hist(last_data, bins=x, edgecolor='k')
kde = mlab.GaussianKDE(last_data)
x2 = np.linspace(min(last_data), max(last_data), 1000)
plt.plot(x2, kde(x2), 'g-', linewidth=2)
plt.xlabel('出生率')
plt.ylabel('频率')
plt.show()

