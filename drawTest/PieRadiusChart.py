from pyecharts import Pie
import pandas as pd

vote_result = pd.read_csv('/home/caisi/PycharmProjects/DataVisualization/data/vote_result.csv')
data_x = vote_result['Areas_of_interest']
data_y = vote_result['Votes']
pie = Pie(title="Annular Chart object for users interest",
          title_pos="left",
          subtitle="The following is vote result.\nreaders are most interested in Finaene and Health care and marketing.")
pie.add("First", data_x,data_y, center=[60,60], legend_orient="vertical", legend_pos="right",
        is_toolbox_show=False, is_label_show=True, radius=[30,80])
pie.render("PieRadiusChart.html")
