import csv
#two variables added for testing

sailor = [("Bob", [2, 4, 1, 1, 2, 5])]
sailors_in_series = [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])]

def series_score(sailor):
    #Take the variable of the sailor + take their worst score
    max_score = sorted(sailor[1])[-1]
    #Get the sum of their series
    total = sum(sorted(sailor[1])) - max_score
    return total


def sort_series(sailors_in_series):
    #Get the scores of the sailors
    #Sort the scores in ascending order
    sailors_in_series = sorted(sailors_in_series, key=lambda x: (series_score(x), x[1][0]))
    #Return the sorted list
    return sailors_in_series

def read_sailor_data():

    with open('sailor_performance.csv', 'r') as csv_file:
        performance_dict = {}
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for line in csv_reader:
            performance_dict[line[0]] = list(line[1], line[2])
    return performance_dict
