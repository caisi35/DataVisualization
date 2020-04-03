import csv
import matplotlib.pyplot as plt


x_data = []
y_data = []
with open("../data/world-population.csv") as f:
    data = csv.reader(f)
    for data_i in data:
        if data.line_num != 1:
            print(data.line_num,data_i)
            x_data.append(data_i[0])
            y_data.append(data_i[1])
plt.plot(x_data[-15:],y_data[-15:],)
plt.xticks(rotation=45)
plt.show()