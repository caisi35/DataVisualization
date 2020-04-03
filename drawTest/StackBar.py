from pyecharts import Bar, Line
import csv


def stack_bar():
    bar = Bar("Stack Bar")
    line = Line("Line")
    with open("../data/hot-dog-places.csv") as f:
        data = list(csv.reader(f))
        x = data[0]
        y1 = data[1]
        y2 = data[2]
        y3 = data[3]
        bar.add("First",x,y1,is_stack=True)
        bar.add("Second",x,y2,is_stack=True)
        bar.add("Third",x,y3,is_stack=True)
        line.add("First",x,y1,is_stack=True)
        line.add("Second",x,y2,is_stack=True)
        line.add("Third",x,y3,is_stack=True)
    return (bar, line)


if __name__ == '__main__':
    bar, line = stack_bar()
    bar.render("stackTopThree.html")
