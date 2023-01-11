from socket import *
s = socket()                    # Skapa ett socket-objekt
s.bind(("10.32.47.8", 12345))   # ändra till din egen IP-adress eller till localhost
s.listen()                      # Vänta på att klient ansluter.
while True:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, addr = s.accept()         # När en klient ansluter
    print("En klient anslöt från adressen", addr)
    conn.close()