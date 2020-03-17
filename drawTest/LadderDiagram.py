from pyecharts import Line


# 1.loading data
data = ['1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005',
        '2006','2007','2008','2009']
data_y = [0.32,0.32,0.32,0.32,0.33,0.33,0.34,0.37,0.37,0.37,0.37,0.39,0.41,0.42,0.44]
# 2.Instantiate the Line object
line = Line("American stamp ladder")
# 3.invocation add(),some Line setup
line.add(name="Price",
         x_axis=data,
         y_axis=data_y,
         is_step=True,
         is_label_show=True,
         yaxis_min=0.3,
         yaxis_max=0.45,
         legand_text_color="red")
# 4.The invocation render(),generate html file
line.render("StampLadder.html")
