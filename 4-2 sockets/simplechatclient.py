# från tidigare exempel
from socket import *
def connect_to_server():
    s = socket()                # Skapa ett socket-objekt
    # Ange IP-adress manuellt
    host = input("Ange serverns IP-adress:")
    port = 12345                # Servern körs på port 12345
    s.connect((host, port))     # Anslut till servern
    return s
s = connect_to_server()

# loopa tills användaren avbryter
while True:
    print("Väntar på meddelande från servern...")
    b = s.recv(1024)            # Ta emot ett meddelande från servern
    msg = b.decode("utf-16")    # Gör om meddelandet från bytekod till vanlig text
    print(msg)
    if msg == "Q":
        break
    msg = input("Skriv något till servern (Avsluta med 'Q'):")
    b = msg.encode("utf-16")
    s.send(b)
    if msg == "Q":
        break
s.close()