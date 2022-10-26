# https://progolymp.se/2018/skolkval/kval18.pdf
# läs input
nbr1 = int(input("Antal 1-grupper ? "))
nbr2 = int(input("Antal 2-grupper ? "))
nbr3 = int(input("Antal 3-grupper ? "))
nbr4 = int(input("Antal 4-grupper ? "))
# beräkna antal soffor
seats_required = nbr4+nbr3  # 4- och 3-grupper kräver varsin soffa
seats_required += (nbr2 // 2)   # två 2-grupper i varje soffa
seats_required += (nbr2 % 2)    # om ojämnt antal 2-grupper krävs en extra soffa
nbr1 -= nbr3    # placera in så många ensamma som möjligt tillsammans med 3-grupper
if nbr1 > 0:    # om det fortfarande finns ensamma kvar
    if nbr2 % 2 > 0:    # om ojämnt antal 2-grupper
        nbr1 -= 2       # placera in två ensamma tillsammans med en 2-grupp
    if nbr1 > 0:    # om det fortfarande finns ensamma kvar
        # placera alla återstående ensamma grupper
        seats_required += nbr1 // 4
        if nbr1 % 4 > 1:    # ej jämnt delbart med 4
            seats_required += 1
# skriv ut resultat
print(seats_required)