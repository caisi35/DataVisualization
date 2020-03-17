from pyecharts import Bar
import pandas as pd
import csv

data = pd.read_csv("/home/caisi/Downloads/presidential_approval_rate.csv")
name = []
y_axis = []
x_axis = ['support','oppose','no_opinion']
bar = Bar(title="voting result",subtitle="...")
style = dict(is_stack=True,xaxis_name="123",xaxis_totate=30,
             legend_pos="right",legend_orient="vertical")
with open("/home/caisi/Downloads/presidential_approval_rate.csv") as f:
    data = csv.reader(f)
    for data_i in data:
        if data.line_num != 1:
            name.append(data_i[0])
            y_axis.append(data_i[1:4])
for i in range(13):
    bar.add(name=name[i], x_axis=x_axis, y_axis=y_axis[i], **style, is_toolbox_show=False)
bar.render("StackBar2.html")