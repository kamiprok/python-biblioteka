import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', database='biblioteka')

print(mydb)

mycursor = mydb.cursor()

mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)

# sql = 'INSERT INTO autorzy (imie, nazwisko) VALUES (%s, %s)'
# val = ('Jan', 'Kochanowski')
# mycursor.execute(sql, val)

# mydb.commit()

query = ('SELECT * FROM autorzy')

mycursor.execute(query)

for x in mycursor:
    print(x)

# sql = 'DELETE FROM autorzy WHERE id_autora = "6"'

# mycursor.execute(sql)

# mydb.commit()
