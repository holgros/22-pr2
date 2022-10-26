# https://progolymp.se/2020/skolkval/kval20.pdf
nbr_participants = input("Antal deltagare ? ")
nbr_participants = int(nbr_participants)
if nbr_participants < 0 or nbr_participants > 10000:
    print("Fel input!")
    exit()

nbr_islands = 0
last_island = 1
current_island = 1

while(nbr_participants > 0):
    nbr_islands += 1
    if nbr_islands == 1 or nbr_islands == 2:
        nbr_participants -= 1
    else:
        new_island = last_island + current_island
        nbr_participants -= new_island
        last_island = current_island
        current_island = new_island

print(nbr_islands)