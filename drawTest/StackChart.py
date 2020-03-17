from pyecharts import Line
import pandas as pd


data = pd.read_csv("../data/us_population_by_age.csv")
years = data['year']
year_under5 = data['year_under5']
year5_19 = data['year5_19']
year20_44 = data['year20_44']
year45_64 = data['year45_64']
year65_above = data['year65above']
line = Line(title="American population Change Chart", width=1000,
            height=600)
style = dict(is_stack=True,xaxis_rotate=30,is_fill=True,is_smooth=True,
             area_opacity=0.5,legend_orient="vertical",legend_pos="right")
line.add("under 5",years,year_under5,area_color='blue',**style)
line.add("year5_19",years,year5_19,area_color='red',**style)
line.add("year20_44",years,year20_44,area_color='#ff3300',**style)
line.add("year45_64",years,year45_64,area_color='rgb(1,1,0',**style)
line.add("year65_above",years,year65_above,area_color='#fa34aa',**style)
line.render("StackChart.html")