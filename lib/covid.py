import csv
import datetime

lines = []
with open('covid1.csv', newline='') as csvfile:
    covidreader = csv.reader(csvfile, delimiter=',')
    deaths_total = 0
    for row in covidreader:
        lines.append(row)

for element in lines:
    if element[0] == '2020-05-18':
        print(element)

if __name__ == "__main__":
    ()
