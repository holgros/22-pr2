class Motorfordon:
    def starta(self):
        print("Vroom!")
class Fyrhjuling:
    def rulla(self):
        print("Rullar!")
class Bil(Motorfordon, Fyrhjuling):
    pass
b = Bil()   
b.starta()  # Vroom!
b.rulla()   # Rullar!
print(isinstance(b, Bil) and isinstance(b, Motorfordon) and isinstance(b, Fyrhjuling))	# True