from pyecharts import Bar
import csv


bar = Bar("Histogram")
x_data = []
y_data = []
with open("/home/caisi/Downloads/hot-dog-contest-winners.csv") as f:
    data = csv.reader(f)
    for data_i in data:
        if data.line_num != 1:
            y_data.append(data_i[2])
            x_data.append(data_i[0])
bar.add("Winners Grade", x_data,y_data)
bar.render("HistogramHotDogContest.html")