import matplotlib.pyplot as plt
import csv
import sys
import datetime
from matplotlib.dates import date2num 

timestamp = []
value = []

with open(sys.argv[1]) as csv_file:
    first = True
    machine_data = csv.reader(csv_file, delimiter=',')
    for row in machine_data:
        timestamp.append(datetime.datetime.strptime(row[0][:-3], '%Y-%m-%d %H:%M:%S.%f'))
        value.append(int(row[2]))

dates = date2num(timestamp)
fig, ax = plt.subplots()
plt.xlabel('Time')
plt.ylabel('Consumption')
plt.title('Dryer')
plt.plot(dates, value)
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.show()
