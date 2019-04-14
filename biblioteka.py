import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', database='biblioteka')

print(mydb)

mycursor = mydb.cursor()

query = 'SHOW TABLES'
mycursor.execute(query)
lista_tabele = []
for i in mycursor:
    lista_tabele.append(i[0])

print(lista_tabele)
if 'autorzy' in lista_tabele:
    print(f'Znaleziono "autorzy" na pozycji {lista_tabele.index("autorzy")}')


query = 'SELECT * from autorzy'
list_autor = [mycursor.execute(query)]
list_autor_2 = []
print(list_autor)
for x in mycursor:
    list_autor_2.append(x)
print(list_autor_2[1][2])

query = 'Show columns from autorzy'
cos = mycursor.execute(query)
lista_autorzy = []
for i in mycursor:
    lista_autorzy.append(i[0])
print(lista_autorzy)
if 'id_autora' in lista_autorzy:
    print(f'Znaleziono "id_autora" na pozycji {lista_autorzy.index("id_autora")}')
input('')

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
