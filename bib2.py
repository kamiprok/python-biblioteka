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

# input(lista_tabele)

autorzy = lista_tabele[0]
ksiazki = lista_tabele[3]
wydawnictwa = lista_tabele[4]
gatunki = lista_tabele[2]
czytelnicy = lista_tabele[1]

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

query = 'show columns from ksiazki'
mycursor.execute(query)
lista_ksiazki = []
for i in mycursor:
    lista_ksiazki.append(i[0])

id_ksiazki = lista_ksiazki[0]
id_autora_ksiazki = lista_ksiazki[1]
wydawnictwo_ksiazki = lista_ksiazki[2]
gatunek_ksiazki = lista_ksiazki[3]
tytul_ksiazki = lista_ksiazki[4]
dostepna_ksiazki = lista_ksiazki[5]

query = 'show columns from wydawnictwa'
mycursor.execute(query)
lista_wydawnictwa = []
for i in mycursor:
    lista_wydawnictwa.append(i[0])

nazwa_wydawnictwa = lista_wydawnictwa[0]

query = 'show columns from gatunki'
mycursor.execute(query)
lista_gatunki = []
for i in mycursor:
    lista_gatunki.append(i[0])

nazwa_gatunku = lista_gatunki[0]

query = 'show columns from czytelnicy'
mycursor.execute(query)
lista_czytelnicy = []
for i in mycursor:
    lista_czytelnicy.append(i[0])

id_czytelnika = lista_czytelnicy[0]
imie_czytelnika = lista_czytelnicy[1]
nazwisko_czytelnika = lista_czytelnicy[2]
miasto_czytelnika = lista_czytelnicy[3]
ulica_czytelnika = lista_czytelnicy[4]
liczba_ksiazek_czytelnika = lista_czytelnicy[5]


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

    print('\nOperacje Czytelnika\n')
    print('7. Wyszukaj po kryterium')
    print('8. Sprawdź dostępność')
    print('9. Zamów')

    print('\nOperacje Bibliotekarza\n')
    print('10. Zrealizuj zamówienie')
    print('11. Potwierdź zwrot')
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
    elif choice == '7':
        menu_wyszukaj()
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


def print_autors():
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


def print_wyd():
    query = f'SELECT * FROM {wydawnictwa}'
    mycursor.execute(query)
    print(dash)
    print('{:<15s}'.format('Nazwa'))
    print(dash)
    for x, y, z in mycursor:
        print('{:<15s}'.format(x))
    print(dash)


def print_gatunek():
    query = f'SELECT * FROM {gatunki}'
    mycursor.execute(query)
    print(dash)
    print('{:<15s}'.format('Nazwa'))
    print(dash)
    for x in mycursor:
        print(x)
    print(dash)


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
        print_autors()
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


def menu_ksiazki():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Książki\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        query = f'SELECT * FROM {ksiazki}'
        mycursor.execute(query)
        print(dash)
        print('{:<10s}'.format('ID KSIĄŻKI'), '{:<10s}'.format('ID AUTORA'), '{:<15s}'.format('WYDAWNICTWO'),
              '{:<15s}'.format('GATUNEK'), '{:<30s}'.format('TYTUŁ'), '{:^10s}'.format('DOSTĘPNA'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:^10d}'.format(x), '{:^10d}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<30s}'.format(b), '{:^10s}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz tytuł książki: ')
        query = f'SELECT * FROM {ksiazki} WHERE {tytul_ksiazki} like "%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:<10s}'.format('ID KSIĄŻKI'), '{:<10s}'.format('ID AUTORA'), '{:<15s}'.format('WYDAWNICTWO'),
              '{:<15s}'.format('GATUNEK'), '{:<30s}'.format('TYTUŁ'), '{:^10s}'.format('DOSTĘPNA'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:^10d}'.format(x), '{:^10d}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<30s}'.format(b), '{:^10s}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        print('Dodawanie nowej ksiązki do bazy\n')
        print_autors()
        print('')
        imie = input('Wpisz ID autora: ')
        os.system('cls')
        print('Dodawanie nowej ksiązki do bazy\n')
        print_wyd()
        print('')
        wyd = input('Wpisz Wydawnictwo: ')
        os.system('cls')
        print('Dodawanie nowej ksiązki do bazy\n')
        print_gatunek()
        gatunek = input('Wpisz Gatunek: ')
        os.system('cls')
        print('Dodawanie nowej ksiązki do bazy\n')
        tytul = input('Podaj Tytuł ksiązki: ')
        try:
            query = f'INSERT INTO `{ksiazki}` (`{id_autora_ksiazki}`, `{wydawnictwo_ksiazki}`, `{gatunek_ksiazki}`, `{tytul_ksiazki}`) VALUES ("{imie}", "{wyd}", "{gatunek}", "{tytul}")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano!')
        except:
            input('nie dodano :(')
    elif choice == '4':
        os.system('cls')
        user_input = input('tytuł książki, którą chcesz usunąć:')
        print('')
        query = f'SELECT * FROM `{ksiazki}` WHERE `{tytul_ksiazki}` like "%{user_input}%"'
        mycursor.execute(query)
        do_usuniecia = []
        print('{:<10s}'.format('ID KSIĄŻKI'), '{:<10s}'.format('ID AUTORA'), '{:<15s}'.format('WYDAWNICTWO'),
              '{:<15s}'.format('GATUNEK'), '{:<30s}'.format('TYTUŁ'), '{:^10s}'.format('DOSTĘPNA'))
        for x, y, z, a, b, c in mycursor:
            print('{:^10d}'.format(x), '{:<10d}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<30s}'.format(b), '{:^10s}'.format(c))
            do_usuniecia.append(x)
        try:
            answer = input('\nPodaj ID książki, którą chcesz usunąć: ')
            mycursor.execute(f'SELECT * FROM {ksiazki} WHERE {id_ksiazki}={answer}')
            myresult = mycursor.fetchone()
            confirm = input(f'Czy na pewno chcesz usunąć {myresult[4]}, ID {myresult[0]} z bazy? [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM `{ksiazki}` WHERE `{id_ksiazki}`="{answer}"'
                mycursor.execute(query)
                mydb.commit()
                input(f'Usunięto {myresult[4]} o ID {myresult[0]} z bazy danych!')
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
        menu_ksiazki()
    menu_ksiazki()


def menu_czytelnicy():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Czytelnicy\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        query = f'SELECT * FROM {czytelnicy}'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'),  '{:^15s}'.format('L. KSIĄŻEK'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:^15d}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz imię lub nazwisko czytelnika: ')
        query = f'SELECT * FROM {czytelnicy} WHERE {imie_czytelnika} like "%{user_input}%" or {nazwisko_czytelnika} like ' \
            f'"%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:<15s}'.format('L. DZIEŁ'))
        print(dash)
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:^10d}'.format(c))
        print(dash)
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        print('Dodawanie nowego Czytelnika do bazy\n')
        imie = input('Wpisz imię: ')
        nazw = input('Wpisz nazwisko: ')
        miasto = input('Wpisz miasto: ')
        ulica = input('Wpisz ulicę: ')
        try:
            query = f'INSERT INTO `{czytelnicy}` (`{imie_czytelnika}`, `{nazwisko_czytelnika}`, `{miasto_czytelnika}`, `{ulica_czytelnika}`) VALUES ("{imie}", "{nazw}", "{miasto}", "{ulica}")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano!')
        except:
            input('nie dodano :(')
    elif choice == '4':
        os.system('cls')
        user_input = input('Wpisz imię lub nazwisko Czytelnika, którego chcesz usunąć: ')
        query = f'SELECT * FROM `{czytelnicy}` WHERE `{imie_czytelnika}` like "%{user_input}%" or `{nazwisko_czytelnika}` like ' \
            f'"%{user_input}%"'
        mycursor.execute(query)
        do_usuniecia = []
        print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
              '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:<15s}'.format('L. DZIEŁ'))
        for x, y, z, a, b, c in mycursor:
            print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:^10d}'.format(c))
            do_usuniecia.append(x)
        try:
            answer = input('Podaj ID Czytelnika, którego chcesz usunąć: ')
            mycursor.execute(f'SELECT * FROM {czytelnicy} WHERE {id_czytelnika}={answer}')
            myresult = mycursor.fetchone()
            confirm = input(f'Czy na pewno chcesz usunąć {myresult[1]} {myresult[2]}, ID {myresult[0]} z bazy? [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM `{czytelnicy}` WHERE `{id_czytelnika}`="{answer}"'
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
        menu_czytelnicy()
    menu_czytelnicy()


def menu_wyszukaj():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Wyszukaj\n')
    print('Wybierz czego szukasz: \n')
    print('1. Autorzy')
    print('2. Książki')
    print('3. Czytelnicy')
    print('4. Wypożyczenia')
    print('5. Wydawnictwa')
    print('6. Gatunki')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nMenu - Wyszukaj - Autorzy\n')
        print('Wybierz kryterium szukania: \n')
        print('1. Imie lub nazwisko')
        print('2. Narodowość')
        print('\nE. Exit')
        choice = input('\nOption: ')
        if choice == '1':
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
            menu_wyszukaj()
        elif choice == '2':
            os.system('cls')
            user_input = input('Wpisz Narodowość autora: ')
            query = f'SELECT * FROM {autorzy} WHERE {narodowosc_autora} like "%{user_input}%"'
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
            menu_wyszukaj()
        elif choice.lower() == 'e':
            main_menu()
        elif choice.lower() == 'exit':
            main_menu()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_wyszukaj()
    # elif choice == '2':
    #     os.system('cls')
    #     print('BIBLIOTEKARZ (Beta)')
    #     print('\nMenu - Wyszukaj - Autorzy\n')
    #     print('Wybierz kryterium szukania: \n')

    elif choice.lower() == 'e':
        menu_wyszukaj()
    elif choice.lower() == 'exit':
        menu_wyszukaj()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_wyszukaj()
    menu_wyszukaj()


main_menu()