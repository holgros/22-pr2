# https://progolymp.se/2022/affisch.pdf
# läs och kontrollera indata
print("Ange varje väggs lampor i tur och ordning med bokstäver, t.ex. 'rgbb' för en röd, en grön, en blå och en till blå lampa")
north = input("Ange översta väggens lampor (från vänster till höger): ")
east = input("Ange högra väggens lampor (uppifrån och ned): ")
south = input("Ange nedersta väggens lampor (från vänster till höger): ")
west = input("Ange vänstra väggens lampor (uppifrån och ned): ")
nbr_cols = len(north)
nbr_rows = len(east)
if len(south) != nbr_cols or len(west) != nbr_rows:
    print("Fel input!")
    exit()
# beräkna antal vita fält genom att loopa genom rektangeln och se hur många fält som det lyser tre lampor på
nbr_whites = 0
for i in range(nbr_rows):
    for j in range(nbr_cols):
        temp = set()    # en mängd (set) är lämpligt eftersom alla element garanterat är olika
        temp.add(north[j])
        temp.add(east[i])
        temp.add(south[j])
        temp.add(west[i])
        print(temp)
        if len(temp) == 3:  # kolla om det finns tre olika element
            nbr_whites += 1
# skriv svaret
print("Svar: ", nbr_whites)