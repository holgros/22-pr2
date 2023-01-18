from socket import *
s = socket()            # Skapa ett socket-objekt
hostname = gethostname()# som körs på den egna datorn
host = gethostbyname(hostname)
port = 12345            # på port 12345.
s.bind((host, port))    # Konfigurera socket-objektet.
s.listen()              # Vänta på att klient ansluter.
print("Servern körs på endpoint", host+":"+str(port))
print("Väntar på att en klient ska ansluta...")
conn, addr = s.accept()     # När en klient ansluter
print("En klient anslöt från adressen", addr)
msg = "Servern säger hej till klienten! Hur mår du idag?"
b = msg.encode("utf-16")    # Gör om meddelandet till bytekod
conn.send(b)                # Skicka meddelandet till klienten
print("Väntar på meddelande från klienten...")
b = conn.recv(1024)         # Ta emot ett meddelande från klienten
msg = b.decode("utf-16")    # Gör om från bytekod till vanlig text
print(msg)
conn.close()                # Stäng anslutningen till klienten