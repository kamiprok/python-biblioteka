import mysql.connector
import os

mydb = mysql.connector.connect(host='localhost', user='root', database='biblioteka')

mycursor = mydb.cursor()
dash = '=' * 40

query = 'SHOW TABLES'
mycursor.execute(query)
lista_tabele = []
for i in mycursor:
    lista_tabele.append(i[0])

autorzy = lista_tabele[0]

query = 'Show columns from autorzy'
mycursor.execute(query)
lista_autorzy = []
for i in mycursor:
    lista_autorzy.append(i[0])

id_autora = lista_autorzy[0]
imie_autora = lista_autorzy[1]
nazwisko_autora = lista_autorzy[2]
narodowosc_autora = lista_autorzy[3]
opis_autora = lista_autorzy[5]

def main_menu():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMain Menu\n')
    print('1. Autorzy')
    print('2. Książki')
    print('3. Czytelnicy')
    print('4. Wypożyczenia')
    print('5. Wydawnictwa')
    print('6. Gatunki')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        menu_autorzy()
    elif choice == '2':
        menu_ksiazki()
    elif choice == '3':
        menu_czytelnicy()
    elif choice == '4':
        menu_wypozyczenia()
    elif choice == '5':
        menu_wydawnictwa()
    elif choice == '6':
        menu_gatunki()
    elif choice.lower() == 'e':
        input('\nPress any key to close...')
        exit()
    elif choice.lower() == 'exit':
        input('\nPress any key to close...')
        exit()
    else:
        input('\nWrong input...')
        os.system('cls')
        main_menu()


def menu_autorzy():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Autorzy\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        query = f'SELECT * FROM {autorzy}'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<10s}'.format('NARODOWOSC'), '{:<10s}'.format('L. DZIEŁ'), '{:<15s}'.format('OPIS'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a),
                  '{:^10d}'.format(b), '{:.50s}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz imię lub nazwisko autora: ')
        query = f'SELECT * FROM {autorzy} WHERE {imie_autora} like "%{user_input}%" or {nazwisko_autora} like ' \
            f'"%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<10s}'.format('NARODOWOSC'), '{:<10s}'.format('L. DZIEŁ'), '{:<15s}'.format('OPIS'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a),
                  '{:^10d}'.format(b), '{:.50s}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        print('Dodawanie nowego autora do bazy\n')
        imie = input('Wpisz imię: ')
        nazw = input('Wpisz nazwisko: ')
        narodowosc = input('Wpisz narodowosc: ')
        opis = input('Podaj krótki opis: ')
        try:
            query = f'INSERT INTO `{autorzy}` (`{imie_autora}`, `{nazwisko_autora}`, `{narodowosc_autora}`, `{opis_autora}`) VALUES ("{imie}", "{nazw}", "{narodowosc}", "{opis}")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano!')
        except:
            input('nie dodano :(')
    elif choice == '4':
        os.system('cls')
        user_input = input('Wpisz imię lub nazwisko autora, którego chcesz usunąć: ')
        query = f'SELECT * FROM `{autorzy}` WHERE `{imie_autora}` like "%{user_input}%" or `{nazwisko_autora}` like ' \
            f'"%{user_input}%"'
        mycursor.execute(query)
        do_usuniecia = []
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a),
                  '{:^10d}'.format(b), '{:.50s}'.format(c))
            do_usuniecia.append(x)
        # answer = input('Czy chcesz usunąć powyższe z bazy? [Y/N]: ')
        # if answer.lower() == 'y':
        #     for i in do_usuniecia:
        #         query = f'DELETE FROM `{autorzy}` WHERE `{id_autora}`="{i}"'
        #         mycursor.execute(query)
        #         mydb.commit()
        #     input('Usunieto!')
        # else:
        #     input('anulowano')
        try:
            answer = input('Podaj ID autora, którego chcesz usunąć: ')
            mycursor.execute(f'SELECT * FROM {autorzy} WHERE {id_autora}={answer}')
            myresult = mycursor.fetchone()
            confirm = input(f'Czy na pewno chcesz usunąć {myresult[1]} {myresult[2]}, ID {myresult[0]} z bazy? [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM `{autorzy}` WHERE `{id_autora}`="{answer}"'
                mycursor.execute(query)
                mydb.commit()
                input(f'Usunięto {myresult[1]} {myresult[2]} z bazy danych!')
            else:
                input('Anulowano...')
        except:
            input('Anulowano...')
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_autorzy()
    menu_autorzy()


main_menu()
