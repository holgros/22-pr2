class Person:
    __bmi = 0   			# privat attribut
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.__bmi = weight/(height**2)
    def getBmi(self):   	# publik åtkomstmetod, s.k. getter-metod
        return self.__bmi
p = Person(70, 1.78)
print(p.getBmi())
#print(p.__bmi)          	# FEL - variabeln __bmi är privat!