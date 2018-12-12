import csv
import random

###############################################################################
#                Problem Solving with Python Coursework                       #
###############################################################################

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
        csv_list = []
        performance_list = {}
        csv_reader = csv.reader(csv_file)
        #Code to append the dictionary with the values in CSV file
        next(csv_reader)
        for row in csv_reader:
            csv_list.append(row)
        count = 1
        for count in range(0, len(csv_list)):
            performance_list.update({csv_list[count][0] : (csv_list[count][1], csv_list[count][2])})
            count += 1

    return performance_list


def generate_performance(performance_list):
    #Blank dictionary for generated performances to be put into
    performance_generated = {}
    #Loop to take each key and value from the sailor data
    read_sailor_data(file_to_read='sailor_performance.csv')
    for i in performance_list.items():
        x = random.normalvariate(int(i[1][0]), int(i[1][1]))
        performance_generated.update({i[0] : x})
    return performance_generated


def calculate_finishing_order(performance_generated):
    x = generate_performance(performance_list)
    finishing_order = []
    #sorts the dictionary in descending order as the larger numbers result in a
    #better position
    y = sorted(performance_generated.items(), key=lambda x: -x[1])
    count = 0
    #the loop adds each sailor into the finishing order list
    for i in y:
        finishing_order.append(y[count][0])
        count+=1
    return finishing_order



performance_list = read_sailor_data(file_to_read='sailor_performance.csv')
sailors_series_generated = {}
#Takes each individual key from the performance_list dictionary and adds it
#to a new dictionary with the value being an empty string
for i in performance_list:
    sailors_series_generated.update({i : []})
#Generate a dictionary where the Key is the sailor in the form of a str and the value as an empty string
count = 0
for count in range(0, 6):
    performance_generated = generate_performance(performance_list)
    finishing_order = calculate_finishing_order(performance_generated)
    #Add scores for sailors to the value in the form of a list
    count += 1
    for i in range(0 , len(finishing_order)):
        #variable to identify each item in the finishing order list
        x = finishing_order[i]
        #the sailors race scores then get added one by one to the sailors_series_generated dictionary
        sailors_series_generated[x].append(i+1)

print(sailors_series_generated)
print(sort_series(sailors_series_generated.items()))
