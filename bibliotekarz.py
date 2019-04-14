import mysql.connector
import os

mydb = mysql.connector.connect(host='localhost', user='root', database='biblioteka')

mycursor = mydb.cursor()
dash = '=' * 40


query = 'Show columns from autorzy'
cos = mycursor.execute(query)
lista_autorzy = []
for i in mycursor:
    lista_autorzy.append(i[0])


def wyszukaj():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Czytelnik - Wyszukaj\n')
    print('Wybierz czego szukasz:\n')
    print('1. Autora')
    print('2. Książki')
    choice = input('\nOption: ')
    if choice == '1':
        wyszukaj_autora()
    if choice == '2':
        wyszukaj_ksiazki()
    elif choice.lower() == 'e':
        menu_czytelnik()
    elif choice.lower() == 'exit':
        menu_czytelnik()
    else:
        input('\nWrong input...')


def wyszukaj_autora():
    try:
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nMenu - Czytelnik - Wyszukaj - Autora\n')
        print('Wybierz kryterium szukania:\n')
        print('1. ID autora')
        print('2. Imie')
        print('3. Nazwisko')
        print('\nE. Exit')
        choice = input('\nOption: ')
        if choice == '1':
            os.system('cls')
            id_autora = input('Wpisz ID autora:')
            query = f'SELECT {lista_autorzy[0]}, imie, nazwisko FROM autorzy WHERE {lista_autorzy[0]}={id_autora}'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'))
            print(dash)
            for x, y, z in mycursor:
                print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z))
            print(dash)
            input('Press any key to continue...')
            menu_czytelnik()

        if choice == '2':
            os.system('cls')
            imie_autora = input('Wpisz IMIĘ Autora:')
            query = f'SELECT id_autora, imie, nazwisko FROM autorzy WHERE imie="{imie_autora}"'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'))
            print(dash)
            for x, y, z in mycursor:
                print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z))
            print(dash)
            input('Press any key to continue...')
            menu_czytelnik()

        if choice == '3':
            os.system('cls')
            nazwisko_autora = input('Wpisz MAZWISKO Autora:')
            query = f'SELECT id_autora, imie, nazwisko FROM autorzy WHERE nazwisko="{nazwisko_autora}"'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'))
            print(dash)
            for x, y, z in mycursor:
                print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z))
            print(dash)
            input('Press any key to continue...')
            menu_czytelnik()

        elif choice.lower() == 'e':
            menu_czytelnik()
        elif choice.lower() == 'exit':
            menu_czytelnik()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_czytelnik()
    except:
        input('Error occurred. Press any key to return to main menu...')
        main_menu()


def wyszukaj_ksiazki():
    try:
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nCzytelnik - Wyszukaj - Książkę\n')
        print('Wybierz kryterium szukania:')
        print('1. ID książki')
        print('2. Tytuł')
        print('3. Autor')
        print('4. Wydawnictwo')
        print('5. Gatunek')
        print('\nE. Exit')
        choice = input('\nOption: ')
        if choice == '1':
            os.system('cls')
            id_ksiazki = input('Wpisz ID książki:')
            query = f'SELECT * FROM ksiazki WHERE id_ksiazki={id_ksiazki}'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<10s}'.format('ID Autora'), '{:<15s}'.format('WYDAWNICTWO'), '{:<10s}'.format('GATUNEK'), '{:<15s}'.format('TYTUŁ'))
            print(dash)
            for x, y, z, a, b in mycursor:
                print('{:<4d}'.format(x), '{:<10d}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a), '{:<15s}'.format(b))
            print(dash)
            input('Press any key to continue...')
            menu_czytelnik()
    except:
        input('Error occurred. Press any key to return to main menu...')
        main_menu()


def menu_czytelnik():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Czytelnik\n')
    print('1. Wyszukaj')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        wyszukaj()
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_czytelnik()


def menu_bibliotekarz():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nBibliotekarz\n')
    print('1. Wypisz Autorów')
    print('2. Wypisz Książki')
    print('3. Wypisz Czytelników')
    print('4. Wypisz Wydawnictwa')
    print('5. Wypisz Gatunki')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        query = f'SELECT * FROM autorzy'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'), '{:<10s}'.format('NARODOWOSC'), '{:<10s}'.format('L. DZIEŁ'), '{:<15s}'.format('OPIS'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a), '{:^10d}'.format(b), '{:.50s}'.format(c))
        print(dash)
        input('Press any key to continue...')
        menu_bibliotekarz()

    if choice == '2':
        os.system('cls')
        query = f'SELECT * FROM ksiazki'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<10s}'.format('ID Autora'), '{:<15s}'.format('WYDAWNICTWO'), '{:<10s}'.format('GATUNEK'), '{:<10s}'.format('TYTUŁ'))
        print(dash)
        for x, y, z, a, b in mycursor:
            print('{:<4d}'.format(x), '{:^10d}'.format(y), '{:<15s}'.format(z), '{:<10s}'.format(a), '{:<30s}'.format(b))
        print(dash)
        input('Press any key to continue...')
        menu_bibliotekarz()

    if choice == '3':
        os.system('cls')
        query = f'SELECT * FROM czytelnicy'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<10s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:<10s}'.format('L. KSIĄŻEK'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:^10d}'.format(c))
        print(dash)
        input('Press any key to continue...')
        menu_bibliotekarz()

    if choice == '4':
        os.system('cls')
        query = f'SELECT * FROM wydawnictwa'
        mycursor.execute(query)
        print(dash)
        print('{:<15s}'.format('NAZWA'), '{:<10s}'.format('KRAJ'), '{:<15s}'.format('MIASTO'))
        print(dash)
        for x, y, z in mycursor:
            print('{:<15s}'.format(x), '{:<10s}'.format(y), '{:<15s}'.format(z))
        print(dash)
        input('Press any key to continue...')
        menu_bibliotekarz()

    if choice == '5':
        os.system('cls')
        query = f'SELECT * FROM gatunki'
        mycursor.execute(query)
        print(dash)
        print('{:<15s}'.format('NAZWA'))
        print(dash)
        for x, in mycursor:
            print('{:<15s}'.format(x))
        print(dash)
        input('Press any key to continue...')
        menu_bibliotekarz()

    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_bibliotekarz()


def main_menu():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMain Menu\n')
    print('{:<20s}{:<20s}'.format('1. Czytelnik', '2. Bibliotekarz'))
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        menu_czytelnik()
    elif choice == '2':
        menu_bibliotekarz()
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

main_menu()
