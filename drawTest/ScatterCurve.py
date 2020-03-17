import numpy as np
import matplotlib.pyplot as plt
import csv


x_data = []
y_data = []
with open("/home/caisi/Downloads/unemployment-rate-1948-2010.csv") as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            y_data.append(float(datarow[3]))
            x_data.append(int(datarow[1]))
plt.scatter(x_data[:],y_data[:],s=30,c='g',marker='o',alpha=0.5)
poly = np.polyfit(x_data,y_data,deg=3)
y_value = np.polyval(poly, x_data)
plt.plot(x_data,y_value)
plt.show()