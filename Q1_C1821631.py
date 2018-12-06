#two variables added for testing

sailor = ("Bob", [2, 4, 1, 1, 2, 5])
sailors_in_series = [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])]

def series_score(sailor):
    #Take the variable of the sailor
    #take their worst score
    max_score = sorted(sailor[1])[-1]
    #Get the sum of their series
    total = sum(sorted(sailor[1])) - max_score
    return total


def sort_series(sailors_in_series):
    #Get the scores of the sailors
    for i in sailors_in_series:
        series_score(sailors_in_series[i])
    sailors_in_series
    #Sort the scores in ascending order

    #Return the sorted list
    return sailors_in_series
