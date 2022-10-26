# https://progolymp.se/2017/skolkval/kval17.pdf
# läs och kontrollera indata
antal_slag = []
antal_banor = 0
try:
    antal_banor = int(input("Antal banor ? "))
    for i in range(antal_banor):
        text = "Bana "+str(i+1)+" ? "
        antal_slag.append(int(input(text)))
    for i in antal_slag:
        if i < 1:
            raise Exception
except:
    print("Fel input!")
    exit()
print(antal_slag)
# beräkna antal slag under/över par
diff = -2*antal_banor-(antal_banor//2)   # varannan 2 varannan 3
for i in antal_slag:
    if i > 7:
        diff += 7
    else:
        diff += i
print("Resultat: " + str(diff))