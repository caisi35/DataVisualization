from pyecharts import Bar
import csv

def hdc_bar():
    bar = Bar("Histogram", page_title="Histogram")
    x_data = []
    y_data = []
    with open("../data/hot-dog-contest-winners.csv") as f:
        data = csv.reader(f)
        for data_i in data:
            if data.line_num != 1:
                y_data.append(data_i[2])
                x_data.append(data_i[0])
    return bar.add("Winners Grade", x_data,y_data, xaxis_rotate=70)
if __name__ == '__main__':
    bar = hdc_bar()
    bar.render("HistogramHotDogContest.html")