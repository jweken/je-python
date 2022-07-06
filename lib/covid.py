import sys
import datetime
import csv

lines = []
file = '.\\docs\\covid.csv'


def get_data_from_file():
    with open(file, newline='') as csvfile:
        covidreader = csv.reader(csvfile, delimiter=',')
        for row in covidreader:
            lines.append(row)


def show_country_totals(country=None):
    """
    This function shows the total record of 'country'
    """
    get_data_from_file()
    for element in lines:
        if element[0] == '2021-03-27' and element[1] == country:
            print(element)


def death_total():
    death = 0
    for element in lines:
        if element[7] != 'Cumulative Confirmed':
            if element[0] == '2021-03-27':
                death += int(element[7])

    print(f'death total: {death}')


if __name__ == "__main__":
    show_country_totals('NL')
