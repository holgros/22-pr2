from socket import *
s = socket()                # Skapa ett socket-objekt
s.connect(("10.32.47.8", 12345))     # Anslut till servern