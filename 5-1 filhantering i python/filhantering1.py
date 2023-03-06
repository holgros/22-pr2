# skriv tre rader i en fil
f = open("exempel.txt", "a")    # "a" står för "append", dvs. skriva utan att radera befintlig text
for i in range(3):
    text = "Skriver siffran " + str(i) + "\n"   # "\n" står för ny rad
    f.write(text)

# öppna och läs fil
f = open("exempel.txt", "r")    # "r" står för read, dvs. läsa
print(f.read())

# stäng fil - görs automatiskt när programmet avslutas, men bra att göra så att det inte blir konflikter under programmets gång
f.close()