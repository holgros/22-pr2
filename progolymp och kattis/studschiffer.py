# https://progolymp.se/2019/skolkval/kval19.pdf
#läs input
N = int(input("Antal rader ? "))
M = int(input("Antal kolumner ? "))
crypto = input("Krypterad text ? ")
crypto_len = len(crypto)
if N < 2 or N > 20 or M < 2 or M > 20 or crypto_len > 30:
    print("Fel input!")
    exit()
answer = ""

# enkla testfall: N=2 och text når inte högerkanten
if N == 2 and crypto_len <= M:
    index = 0
    while len(answer) < crypto_len:
        start = index
        while index < crypto_len:
            answer += crypto[index]
            index += (crypto_len//2 + 1)
        index = start+1
    print(answer)

    '''         svårare testfall N>2
    strategi:   Konstruera först en "nyckel" genom att studsa runt genom en 2d-array och anteckna ordningstal.
                När vi väl har konstruerat denna nyckel så kan vi lätt avkoda chiffret.'''
else:
    # konstruera en 2d-array som innehåller siffror motsvarande respektive rutas ordningstal
    order = []
    for n in range(N):
        temp = []
        for m in range(M):
            temp.append(None)
        order.append(temp)
    k = 0
    n = 0
    m = 0
    downwards = True
    rightwards = True
    while k < crypto_len:
        if order[n][m] == None: # om det inte redan står en bokstav i rutan
            order[n][m] = k
            k += 1
        if n == N-1:    # studsa mot nederkanten
            downwards = False
        if n == 0:      # studsa mot överkanten
            downwards = True
        if m == M-1:    # studsa mot högerkanten
            rightwards = False
        if m == 0:      # studsa mot vänsterkanten
            rightwards = True
        if downwards:
            n += 1
        else:
            n -= 1
        if rightwards:
            m += 1
        else:
            m -= 1
    # avkoda chiffret med hjälp av ovan konstruerade 2d-array
    decrypted = []
    for k in range(crypto_len):
        decrypted.append("")
    k = 0
    for n in range(N):
        for m in range(M):
            position = order[n][m]
            if position != None:
                decrypted[position] = crypto[k]
                k += 1
    output = ""
    for k in decrypted:
        output += k
    print(output)
    # print(order) # kommentera bort för att se hur 2d-arrayen är konstruerad