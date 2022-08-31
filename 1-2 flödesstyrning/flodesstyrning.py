# Demo av enkla if-, else- och elif-satser
x = 10
s = "Hej"
if x < 10 or s == "Nej":
    print("Foo")
elif s == "Hej":
    print("Bar")            # Hit går programflödet
else:
    print("Baz")

# Demo av enkla loopar
arr = ["Foo", "Bar", "Baz"]
for i in range(3):
    print(arr[i])
set = {"One", "Two", "Three"}
for i in set:
    print(i)    # OBS: en mängd (set) är inte ordnat, så vi kan t.ex. få utskrften "Two, One, Three" istället för "One, Two, Three"
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
for i in dic:
    print("Huvudstaden i", i, "heter", dic[i])  # dictionaries är ordnade, så utskriften börjar med Sverige och slutar med Finland

# while-loop med break och continue
x = 0
while x < 10:
    x += 1
    if x == 2:
        continue
    if x == 5:
        break
    print(x)	# ger utskrift 1 3 4

# demo undantagshantering
proceed = True
while proceed:
    try:
        x = input("Ange ett heltal: ")
        x = int(x)
        proceed = False
    except:
        print("Du måste ange ett heltal!")
    else:
        print("Input OK!")
    finally:
        print("Detta meddelande skrivs ut vad som än händer.")
