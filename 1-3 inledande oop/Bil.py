class Bil:      # implementera klassen bil, dvs. en "form" som alla enskilda bilar skapas av
    antalBilar = 0                      # statiskt attribut
    def __init__(self, speed, brand):   # bilens konstruktor
        self.speed = speed
        self.brand = brand
        Bil.antalBilar += 1             # inkrementera statiskt attribut
    def honk(self):                     # en Bil-metod
        print("TUUT!!")
    def drive(self):                    # en till Bil-metod
        print("Bilen körs i", self.speed, "kilometer i timmen.")
    @staticmethod
    def milestokm(miles):
        return 1.6093*miles
bil1 = Bil(50, "Volvo")
bil1.honk()
bil1.drive()
bil2 = bil1             # variabeln bil2 "pekar" på samma objekt som bil1 - vi har alltså inte skapat något nytt objekt
bil2.speed = 70         # ändrar både bil1 och bil2
print(bil1.speed)       # 70

# icke-statiska metoder kan inte anropas utan att man först skapar ett objekt
#honk()      # fel!!
#Bil.honk()  # också fel!!

# en statisk metod kan anropas utan att man först skapar ett objekt;
# observera punktnotation med klassens namn först!
print(Bil.milestokm(15))    # 24.1395

# hur många bilar har skapats?
bil2 = Bil(60, "Volkswagen")
bil3 = Bil(80, "Saab")
print(Bil.antalBilar)       # 3