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

query = ('SELECT id_autora,imie,nazwisko FROM autorzy')

mycursor.execute(query)

print('SELECT id_autora,imie,nazwisko FROM autorzy: \n')
dash = '=' * 40
print(dash)
print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'))
print(dash)
for x, y, z in mycursor:
    print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z))
print(dash)

# sql = 'DELETE FROM autorzy WHERE id_autora = "6"'

# mycursor.execute(sql)

# mydb.commit()
