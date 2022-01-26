import os
import csv

with open(f"{os.path.dirname(__file__)}/weather.csv") as csvfile:
    data = list(csv.reader(csvfile))
    temperatures = [ int(data[i][1]) for i in range(1, len(data)) ]
    
print(temperatures)