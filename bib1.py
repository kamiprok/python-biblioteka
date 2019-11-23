import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='Biblioteka'
)

print('')
print(mydb)

print('')
mycursor = mydb.cursor()

mycursor.execute('show databases')

for x in mycursor:
    print(x)

print('')
mycursor.execute('show tables')

for x in mycursor:
    print(x)

print('')
mycursor.execute('select * from ksiazki')

for x in mycursor:
    print(x)

print('')
mycursor.execute('show columns from ksiazki')

for x in mycursor:
    print(x)

print('')
mycursor.execute('select id_autora, imie, nazwisko from autorzy')

for x in mycursor:
    print(x)
