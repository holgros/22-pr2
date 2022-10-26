# https://progolymp.se/2022/skolkval/kval22.pdf
# läs input och dela upp i rader och kolumner
N = int(input("N ?"))
rader = []
rad_index = []
kolumn_index = []
for i in range(N):
    rader.append(input("Rad " + str(i+1) + " ?"))
    if not "." in rader[i]:
        rad_index.append(i)
    elif kolumn_index == []:
        for j in range(len(rader[i])):
            if rader[i][j] != ".":
                kolumn_index.append(j)
print("Input:", str(rader))

# övergripande strategi: måla "baklänges" ett antal gånger motsvarande antal rader + antal kolumner
ordning = ""
farger = ""
antal_iterationer = len(rad_index) + len(kolumn_index)
for iteration in range(antal_iterationer):
    hittat_rad = False
    for i in range(len(rad_index)):
        if not "." in rader[rad_index[i]]:
            if not "V" in rader[rad_index[i]] or not "S" in rader[rad_index[i]]:
                # en hel rad med bara "S" eller bara "V"
                if "V" in rader[rad_index[i]]:
                    farger += "V"
                else:
                    farger += "S"
                hittat_rad = True
                ordning += str(rad_index[i] + 1)
                # uppdatera raderna genom att återställa hur de såg ut innan denna rad målades
                for j in range(len(rader[0])):
                    bokstavslista = list(rader[rad_index[i]])
                    if not j in kolumn_index:
                        bokstavslista[j] = "."
                    else:
                        bokstavslista[j] = "?"    # antingen S eller V
                    rader[rad_index[i]] = "".join(bokstavslista)
                rad_index.pop(i)
                break
    if hittat_rad:
        continue
    # leta efter en kolumn ifall ingen rad har hittats
    kolumner = []
    for i in range(len(kolumn_index)):
        kolumner.append("")
        for j in range(len(rader)):
            kolumner[i] += rader[j][kolumn_index[i]]
    for i in range(len(kolumner)):
        if not "V" in kolumner[i] or not "S" in kolumner[i]:
            # en hel kolumn med bara "S" eller bara "V"
            if "V" in kolumner[i]:
                farger += "V"
            else:
                farger += "S"
            bokstaver = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
            ordning += bokstaver[kolumn_index[i]]
            # uppdatera raderna genom att återställa hur de såg ut innan denna rad målades
            for j in range(N):
                bokstavslista = list(rader[j])
                if "." in rader[j]:
                    bokstavslista[kolumn_index[i]] = "."
                else:
                    bokstavslista[kolumn_index[i]] = "?"
                rader[j] = "".join(bokstavslista)
            kolumn_index.pop(i)
            break
    
# skriv ut svaret
print("Ordning:", str(ordning[::-1]))   # baklänges!
print("Färger:", str(farger[::-1]))     # dito!