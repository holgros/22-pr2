# skriv över filens innehåll
f = open("exempel.txt", "w")    # "w" står för "write", dvs. skriv över allt innehåll
f.write("Skriver över all text!")
# läs filen igen och kolla att innehållet skrivits över
f = open("exempel.txt", "r")
print(f.read())
f.close()