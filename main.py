#MapPlot.py
#Name:
#Date:
#Assignment:


import county_demographics
county_demographics = county_demographics.get_report()

num_items = len(county_demographics)
state_list = []
population_list = []
for spot in range(num_items):
    population = county_demographics [spot]["Population"]["2020 Population"]
    states = county_demographics[spot]["State"]
    if states in ["NE", "SD", "CO", "WY", "IO", "OH", "ND"]:
    #total_score = county_demographics[spot]["data"]["population"]["total"]
        print ("State_list")
        state_list.append(states)
        population_list.append(population)
    #print(states)
    #print (population)


import matplotlib.pyplot as plt
plt.plot(state_list, population_list, "ro")
plt.ylabel('population')
plt.xlabel("states")
plt.savefig("output")




