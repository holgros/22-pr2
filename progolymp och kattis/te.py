# https://progolymp.se/2020/skolkval/kval20.pdf
# läs input
nbr_bags = input("Antal påsar ? ")
nbr_bags = int(nbr_bags)
nbr_people = input("Antal personer ? ")
nbr_people = int(nbr_people)
if nbr_bags < 1 or nbr_bags > 10 or nbr_people < 1 or nbr_people > 100:
    print("Fel input!")
    exit()

# beräkna antal tekannor
capacities = []
for i in range(nbr_bags):
    question = "Påse " + str(i+1) + " räcker till ?"
    capacity = input(question)
    capacity = int(capacity)
    if capacity < 1 or capacity > 100:
        print("Fel input!")
        exit()
    capacities.append(capacity)

# koka te åt alla
nbr_pots = 0
while nbr_people > 0:
    nbr_pots += 1
    brew = False
    for i in range(nbr_bags):
        if capacities[i] > 9:
            capacities[i] -= 10
            nbr_people -= 10
            brew = True
            break
    if not brew:
        max = 0
        max_index = None
        for i in range(nbr_bags):
            if capacities[i] > max:
                max = capacities[i]
                max_index = i
        nbr_people -= capacities[max_index]
        capacities[max_index] = 0

print(nbr_pots)