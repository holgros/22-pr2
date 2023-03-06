# hantera modulen os, som bl.a. kan skapa och radera mappar
import os
try:
    os.mkdir("undermapp")
    print("Skapat undermapp!")
except: # blir fel ifall t.ex. mappen redan finns
    print("Något gick fel!")
# öppna fil i undermapp
f = open("undermapp/annat_exempel.txt", "a")
f.write("Skriver till textfil i undermapp")
f.close()   # OBS - måste stänga innan den raderas
os.remove("undermapp/annat_exempel.txt")    # ta bort fil
os.rmdir("undermapp")