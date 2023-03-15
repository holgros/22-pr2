import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",  # standardanvändarnamn för XAMPP
  password="",  # dito lösenord (en tom sträng)
  database="Prog2"  # byt namn om din databas heter något annat
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

# Skriva till databasen
sql = "INSERT INTO Elever (id, fornamn, efternamn, klass) VALUES (%s, %s, %s, %s)"
val = (3, "Terry", "Jones", "TE19C")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Läsa från databasen
mycursor.execute("SELECT * FROM Elever")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

