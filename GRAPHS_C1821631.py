import matplotlib.pyplot as plt
import numpy as np
from Q1_C1821631 import *
###############################################################################
#              Graph's to show results of generate performances               #
###############################################################################







def Races_won():
    performance_list = read_sailor_data(file_to_read='sailor_performance.csv')
    sailors_series_generated = {}
    for i in performance_list:
        sailors_series_generated.update({i : []})
    count=0
    for count in range(0,1000):
        performance = generate_performance(performance_list)
        finishing_order = calculate_finishing_order(performance)
        count += 1
        for i in range(0 , len(finishing_order)):
            x = finishing_order[i]
            sailors_series_generated[x].append(i+1)
    list_1 = []
    for key, value in sailors_series_generated.items():
        list_1.append([key, value])
        list_average = [[i[0], sum(i[1])/1000] for i in list_1]
    print(list_average)
        

y_pos = Races_won()
bars = read_sailor_data(file_to_read='sailor_performance.csv')
bars = [bars.keys()]
order = sorted(y_pos, key = lambda x: (x[0]))


plt.bar(order , y_pos , align='center', alpha=0.5)
plt.xticks(order , y_pos)
plt.xlabel('Sailors In Series')
plt.ylabel('Average Position')
fig.title('Average Performance of Sailors')

plt.show()
