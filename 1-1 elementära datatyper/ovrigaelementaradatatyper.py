# strängar och tupplar
s = "Hej på dig!"
print(len(s))   # 11
print(s[0])     # "H"
print(s[10])    # "!"
print(s.upper())    # inbyggd metod till sträng, returnerar en sträng med stora bokstäver (men ändrar inte den ursprungliga textsträngen)
print("Hej på dig!"[2]) # "j"
tuple = s.partition("på")   # skapar en tippel bestående av tre element
print(tuple)        # ("Hej", "på", "dig!")
array = ["Hej", "på", "dig!"]   # skapar ett fält liknande ovanstående tippel
array[2] = "mig!"   # OK! Fält kan ändras.
#tuple[2] = "mig!"  # FEL! Tipplar kan INTE ändras när de väl har skapats!

# en dictionary (associativt fält) förknipar varje nyckel med ett värde
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
print(dic["Sverige"])               # "Stockholm"
print(dic["Norge"])                 # "Oslo"
print(dic["Finland"])               # "Helsingfors"
#print(dic["Danmark"])              # KeyError
# metoder för associativa fält
dic.update({"Estland": "Tallinn"})	# lägga till ett nyckel-värdepar
dic.pop("Sverige")			        # ta bort nyckel-värdeparet med nyckeln "Sverige"

# nycklar behöver inte vara strängar
dic = {1: "Foo", "Bar": "Baz", True: False} # OK!

# booleska variabler
bool = True or 0
print(bool)         # True
bool = True and 1
print(bool)         # 1
bool = not False or ""
print(bool)         # True
bool = False and ""
print(bool)         # False
bool = True and ""
print(bool)         # tom sträng

# mängd (set)
s = set()   # anropa konstruktorn
s.add("Äpple")
s.add("Banan")
s.add("Päron")
s.add("Äpple")      # Vi har redan ett äpple
print(s)            # {"Banan", "Päron", "Äpple"}
