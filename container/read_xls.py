import pandas as pd
import os

filepath = os.path.abspath('/home/caisi/PycharmProjects/GoodBooks/GoodBooks.xls')

data = pd.read_excel(filepath, sheet_name='原始数据')
pd.set_option('max_columns',6)

data.to_csv('./GoodBooks.csv', index=False)