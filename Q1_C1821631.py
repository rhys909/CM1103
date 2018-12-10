import csv
import random
#two variables added for testing

sailor = [("Bob", [2, 4, 1, 1, 2, 5])]
sailors_in_series = [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])]

def series_score(sailor):
    #Take the variable of the sailor + take their worst score
    max_score = (sailor[1].sort())[-1]
    #Get the sum of their series
    total = sum(sorted(sailor[1])) - max_score
    return total


def sort_series(sailors_in_series):
    #Get the scores of the sailors
    #Sort the scores in ascending order
    sailors_in_series = sorted(sailors_in_series, key=lambda x: (series_score(x), x[1][0]))
    #Return the sorted list
    return sailors_in_series

def read_sailor_data(file_to_read='sailor_performance.csv'):
    #Code to read the CSV file
    with open(file_to_read, 'r') as csv_file:
        performance_dict = {}
        csv_reader = csv.reader(csv_file)
        #Code to append the dictionary with the values in CSV file
        next(csv_reader)
        for line in csv_reader:
            performance_dict[line[0]] = list(line[1], line[2])

    return performance_dict

def generate_performance(performance_dict):
    #Blank dictionary for generated performances to be put into
    performance_generated = {}
    #Loop to take each key and value from the sailor data
    read_sailor_data(file_to_read='sailor_performance.csv')
    for key, value in performance_dict:
        performance_generated[key] = performance_generated[random.normalvgariate(int(value[0]), int(value[1]))]
    return performance_generated

def calculate_finishing_order(performance_generated):
    generate_performance(performance_dict)
    finishing_order = [key for (key, value) in sorted(performance_generated.value())]
    return finishing_order

name= input(">>> Name of the series?")
def series(name):
    read_sailor_data(file_to_read='sailor_performance.csv')
    count = 0
    sailors_series_generated = {}
    for key in peformance_dict:
        sailors_series_generated[key] = sailors_series_generated[list()]
        for count in range(0, 5):
        #Add scores for sailors to the value in the form of a list
        generate_performance(performance_dict)
        calculate_finishing_order(performance_generated)
        count += 1
    return sailors_series_generated
