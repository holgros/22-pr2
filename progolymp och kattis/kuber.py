# https://progolymp.se/2019/skolkval/kval19.pdf
# läs input, loopa och skriv svaret
N = int(input("Talet N ? "))
if N < 2 or N > 40:
    print("Fel input!")
else:
    answer = 0
    for i in range(N+1):
        answer += i**3
    print("Antal:", answer)