def twice(x):
    print(x+x)
twice(2)
twice("2")
twice(2.0)
print(2.0+2)
#print(2+"2") #Fel!

class Aeroplane:
    static_attribute = "Statiskt!"
    def fly(self):
        print("Flyger!")
    def __init__(self):
        self.max_altitude = 10000
        self.__private_attribute = "Privat!"
    def get_private_attribute(self):
        return self.__private_attribute
boeing = Aeroplane()
print(boeing.max_altitude)
#print(boeing.__private_attribute) #Fel!
print(boeing.get_private_attribute())
print(Aeroplane.static_attribute)

def subtract_one(x):
    x -= 1
x = 1
subtract_one(x)
print(x)

try:
    x = int("Blargh!")
    print("Succé!")
except:
    print("Fiasko!")
finally:
    print("Hej då!")
