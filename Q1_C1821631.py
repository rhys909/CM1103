def series_score(sailor):
    #Take the variable of the sailor
    sailor.sort()
    #take their worst score
    sailor.pop(-1)
    #Get the sum of their series
    total = 0
    for i in sailor:
        total  += i
    return total
def sort_series(sailors_in_series):
    #Get the scores of the sailors
    for sailor in sailors_in_series:
        for i in sailor:

    #Sort the scores in ascending order
    sorted(sailors_in_series.value())
    #Return the sorted list
    return sailors_in_series
