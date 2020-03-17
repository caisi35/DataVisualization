import csv
import matplotlib.pyplot as plt


y_data = []
x_data = []
with open("/home/caisi/Downloads/subscribers.csv") as f:
    data = csv.reader(f)
    for data_i in data:
        if data.line_num != 1:
            y_data.append(int(data_i[1]))
            x_data.append(str(data_i[0])[3:5])
        print(data_i)
print(y_data)
plt.scatter(x=x_data,y=y_data,s=50,c='r',marker='o',alpha=0.5)
plt.show()