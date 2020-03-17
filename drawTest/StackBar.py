from pyecharts import Bar
import csv


bar = Bar("Stack Bar")
with open("/home/caisi/Downloads/hot-dog-places.csv") as f:
    data = list(csv.reader(f))
    x = data[0]
    y1 = data[1]
    y2 = data[2]
    y3 = data[3]
    bar.add("First",x,y1,is_stack=True)
    bar.add("Second",x,y2,is_stack=True)
    bar.add("Third",x,y3,is_stack=True)
    bar.render("stackTopThree.html")
