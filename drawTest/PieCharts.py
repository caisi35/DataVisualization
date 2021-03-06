from pyecharts import Pie
import pandas as pd


def pie_charts():

    vote_result = pd.read_csv('/home/caisi/PycharmProjects/DataVisualization/data/vote_result.csv')
    data_x = vote_result['Areas_of_interest']
    data_y = vote_result['Votes']
    pie = Pie(title="Pie object for user interest",
              title_pos="left",
              subtitle="The following is vote result.\nreaders are most interested in Finaene and Health care and marketing.")
    return pie.add("First", data_x,data_y, center=[60,60], legend_orient="vertical", legend_pos="right",
            is_toolbox_show=False, is_label_show=True)


if __name__ == '__main__':
    pie = pie_charts()
    pie.render("PieCharts.html")
