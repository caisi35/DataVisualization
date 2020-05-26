from pyecharts import Bar, Line, Polar
import csv


def hot_dog_polar_lzx():
    polar_lzx = Polar('各年度热狗大胃王比赛前三名成绩-李兆旭', height=600)
    with open('../data/hot-dog-places.csv') as f:
        data_lzx = list(csv.reader(f))
    style_lzx = dict(type='barAngle', legend_orient='vertical', legend_pos='right')
    polar_lzx.add("First", angle_data=data_lzx[0], data=data_lzx[1], is_stack=True, **style_lzx)
    polar_lzx.add("Second", angle_data=data_lzx[0], data=data_lzx[2], is_stack=True, **style_lzx)
    polar_lzx.add("Third", angle_data=data_lzx[0], data=data_lzx[3], is_stack=True, **style_lzx)
    polar_lzx.render('hot-dog-polar.html')


def stack_bar():
    bar = Bar("Stack Bar")
    line = Line("Line")
    with open("../data/hot-dog-places.csv") as f:
        data = list(csv.reader(f))
        x = data[0]
        y1 = data[1]
        y2 = data[2]
        y3 = data[3]
        bar.add("First", x, y1, is_stack=True)
        bar.add("Second", x, y2, is_stack=True)
        bar.add("Third", x, y3, is_stack=True)
        line.add("First", x, y1, is_stack=True)
        line.add("Second", x, y2, is_stack=True)
        line.add("Third", x, y3, is_stack=True)
    return (bar, line)


if __name__ == '__main__':
    hot_dog_polar_lzx()
    # bar, line = stack_bar()
    # bar.render("stackTopThree.html")
