from pyecharts import Bar
import pandas as pd


def stack_bar_chart2():
    data = pd.read_csv('../data/presidential_approval_rate.csv')
    data_x = data['political_issue']
    data_y1 = data['support']
    data_y2 = data['oppose']
    data_y3 = data['no_opinion']
    bar = Bar(title='vote result', subtitle="It is subtitle.")
    style = dict(is_stack=True, xaxis_name="Voting Classification", xaxis_rotate=30)
    bar.add(name="support",x_axis=data_x,y_axis=data_y1,**style)
    bar.add(name="oppose",x_axis=data_x,y_axis=data_y2,**style)
    bar.add(name="no_opinion",x_axis=data_x,y_axis=data_y3,**style)
    return bar


if __name__ == '__main__':
    bar = stack_bar_chart2()
    bar.render("StackBarChart.html")