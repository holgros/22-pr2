'''
# Ärvda metoder
class Fordon:
    def kör(self):
        print("Nu kör vi!")
class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")
b = Bil()
b.kör()     # anropar en Fordon-metod i ett Bil-objekt
b.tuta()    # anropar en Bil-metod
f = Fordon()
f.kör()
#f.tuta() NEJ - ett fordon är inte nödvändigtvis en bil och kan därför inte tuta
'''

# Överskuggning med ändrad signatur
class Superclass:
    def hej(self):
        print("Hej från Super!")
class Subclass(Superclass):
    def hej(self, x):   # OBS - vi kräver nu en inparameter
        print("Hej från Sub!")
        print("input = ", x)
sup = Superclass()
sup.hej()   # Hej från Super!
sub = Subclass()
sub.hej(2)   # Hej från Sub!
#sub.hej()   # NEJ - hej har nu en annan signatur