class Fordon:
    def åka(self):
        print("Fordon åker!")
class Motorfordon(Fordon):
    def åka(self):  # överskuggad metod
        print("Motorfordon åker!")
class Fyrhjuling(Fordon):
    def åka(self):  # överskuggad metod
        print("Fyrhjuling åker!")
class Bil(Fyrhjuling, Motorfordon): # argumentens ordning spelar roll!
    pass
b = Bil()
b.åka() # Fyrhjuling eller Motorfordon åker?