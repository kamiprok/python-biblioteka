import mysql.connector
import os
from datetime import datetime, timedelta, date

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
wypozyczenia = lista_tabele[5]

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
kraj_wydawnictwa = lista_wydawnictwa[1]
miasto_wydawnictwa = lista_wydawnictwa[2]

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

query = 'show columns from wypozyczenia'
mycursor.execute(query)
lista_wypozyczenia = []
for i in mycursor:
    lista_wypozyczenia.append(i[0])

id_wypozyczenia = lista_wypozyczenia[0]
id_czytelnika_wypozyczenia = lista_wypozyczenia[1]
id_ksiazki_wypozyczenia = lista_wypozyczenia[2]
data_zamowienia_wypozyczenia = lista_wypozyczenia[3]
data_wypozyczenia_wypozyczenia = lista_wypozyczenia[4]
data_zwrotu_wypozyczenia = lista_wypozyczenia[5]
status_wypozyczenia = lista_wypozyczenia[6]


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

    print('\nOperacje Bibliotekarza\n')
    print('7. Wyszukaj po kryterium')
    print('8. Sprawdź dostępność')
    print('9. Zmień status')

    print('\n0. Custom')

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
    elif choice == '8':
        menu_sprawdz_dostepnosc()
    elif choice == '9':
        menu_zmien_status()
    elif choice == '0':
        menu_custom()
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
    print('{:<20s}'.format('NAZWA WYDAWNICTWA'), '{:<10s}'.format('KRAJ'), '{:<10s}'.format('MIASTO'))
    print(dash)
    for x, y, z in mycursor:
        print('{:<20s}'.format(x), '{:<10s}'.format(y), '{:<10s}'.format(z))
    print(dash)


def print_gatunek():
    query = f'SELECT * FROM {gatunki}'
    mycursor.execute(query)
    print(dash)
    print('{:<15s}'.format('Nazwa'))
    print(dash)
    for x in mycursor:
        print(x[0])
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
        query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora'
        mycursor.execute(query)
        print(dash)
        print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
              '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
        print(dash)
        for x, y, z, a, b, c, d in mycursor:
            print('{:^5d}'.format(x), '{:<25s}'.format(y+' '+z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
        print(dash)
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz tytuł książki: ')
        query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {tytul_ksiazki} like "%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
              '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
        print(dash)
        for x, y, z, a, b, c, d in mycursor:
            print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                  '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
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


def menu_wypozyczenia():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Wypożyczenia\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        query = f'SELECT * FROM {wypozyczenia}'
        mycursor.execute(query)
        print(dash)
        print('{:^4s}'.format('ID'), '{:^10s}'.format('ID KSIĄŻKI'), '{:^15s}'.format('ID CZYTELNIKA'),
              '{:<20s}'.format('DATA ZAMÓWIENIA'), '{:<20s}'.format('DATA WYPOŻYCZENIA'), '{:<20s}'.format('DATA ZWROTU'), '{:<15s}'.format('STATUS'))
        print(dash)
        for x, y, z, a, b, c, d in mycursor:
            print('{:^4d}'.format(x), '{:^10d}'.format(y), '{:^15d}'.format(z), '{:<20}'.format(a.strftime('%Y-%m-%d')), '{:<20s}'.format(b.strftime('%Y-%m-%d')), '{:<20s}'.format(c.strftime('%Y-%m-%d')), '{:<15}'.format(d))
        print(dash)
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        try:
            user_input = input('Wprowadź datę wypożyczenia[YYYY-MM-DD]: ')
            query = f'SELECT * FROM {wypozyczenia} WHERE {data_wypozyczenia_wypozyczenia} like "%{user_input}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^4s}'.format('ID'), '{:^15s}'.format('ID CZYTELNIKA'), '{:^10s}'.format('ID KSIĄŻKI'),
                  '{:<20s}'.format('DATA ZAMÓWIENIA'), '{:<20s}'.format('DATA WYPOŻYCZENIA'),
                  '{:<20s}'.format('DATA ZWROTU'), '{:<15s}'.format('STATUS'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^4d}'.format(x), '{:^15d}'.format(y), '{:^10d}'.format(z), '{:<20}'.format(a.strftime('%Y-%m-%d')),
                      '{:<20s}'.format(b.strftime('%Y-%m-%d')), '{:<20s}'.format(c.strftime('%Y-%m-%d')),
                      '{:<15}'.format(d))
            print(dash)
        except:
            print('Something went wrong...')
            menu_wypozyczenia()
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        try:
            print('Dodawanie nowego Wypożyczenia: ')
            czytelnik = input('Podaj ID czytelnika: ')
            ksiazka = input('Podaj ID wypożyczanej książki: ')
            now = date.today()
            now_15 = now + timedelta(days=15)
            print(now)
            now_string = str(now)
            print(now_15)
            print(now_string)
            query = f'INSERT INTO {wypozyczenia} ({id_czytelnika_wypozyczenia}, {id_ksiazki_wypozyczenia}, {data_zamowienia_wypozyczenia}, {data_wypozyczenia_wypozyczenia}, {data_zwrotu_wypozyczenia}, {status_wypozyczenia}) VALUES ({czytelnik}, {ksiazka}, "{now_string}", "{now}", "{now_15}", "wypożyczona")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano do bazy')
        except:
            input('Coś poszło nie tak...')
    elif choice == '4':
        try:
            os.system('cls')
            user_input = input('Podaj ID wypożyczenia, które chcesz usunąć: ')
            query = f'SELECT * FROM `{wypozyczenia}` WHERE `{id_wypozyczenia}` like "%{user_input}%"'
            mycursor.execute(query)
            print('{:^4s}'.format('ID'), '{:^15s}'.format('ID CZYTELNIKA'), '{:^10s}'.format('ID KSIĄŻKI'),
                  '{:<20s}'.format('DATA ZAMÓWIENIA'), '{:<20s}'.format('DATA WYPOŻYCZENIA'),
                  '{:<20s}'.format('DATA ZWROTU'), '{:<15s}'.format('STATUS'))
            for x, y, z, a, b, c, d in mycursor:
                print('{:^4d}'.format(x), '{:^15d}'.format(y), '{:^10d}'.format(z), '{:<20}'.format(a.strftime('%Y-%m-%d')),
                      '{:<20s}'.format(b.strftime('%Y-%m-%d')), '{:<20s}'.format(c.strftime('%Y-%m-%d')),
                      '{:<15}'.format(d))

            confirm = input(f'Czy na pewno chcesz usunąć wypożyczenie z bazy? [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM `{wypozyczenia}` WHERE `{id_wypozyczenia}`="{user_input}"'
                mycursor.execute(query)
                mydb.commit()
                input(f'Usunięto z bazy danych!')
            else:
                input('Anulowano...')
        except:
            input('Wystąpił nieoczekiwany problem...')
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_wypozyczenia()
    menu_wypozyczenia()


def menu_wydawnictwa():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Wydawnictwa\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        print_wyd()
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz nazwę szukanego wydawnictwa: ')
        query = f'SELECT * FROM {wydawnictwa} WHERE {nazwa_wydawnictwa} like "%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:<20s}'.format('NAZWA WYDAWNICTWA'), '{:<10s}'.format('KRAJ'), '{:<10s}'.format('MIASTO'))
        print(dash)
        for x, y, z in mycursor:
            print('{:<20s}'.format(x), '{:<10s}'.format(y), '{:<10s}'.format(z))
        print(dash)
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        print('Dodawanie nowego wydawnictwa\n')
        nazwa = input('Podaj nazwę wydawnictwa: ')
        kraj = input('Podaj kraj pochodzenia wydawnictwa: ')
        miasto = input('Podaj masto pochodzenia wydawnictwa: \n')
        try:
            query = f'INSERT INTO {wydawnictwa} ({nazwa_wydawnictwa}, {kraj_wydawnictwa}, {miasto_wydawnictwa}) VALUES ("{nazwa}", "{kraj}", "{miasto}")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano!')
        except:
            input('Nie dodano, something went wrong...')
            menu_wydawnictwa()
    elif choice == '4':
        try:
            os.system('cls')
            answer = input('Podaj nazwę wydawnictwa, które chcesz usunąć: ')
            query = f'SELECT * FROM {wydawnictwa} WHERE {nazwa_wydawnictwa.lower()}="{answer.lower()}"'
            mycursor.execute(query)
            print(dash)
            print('{:<20s}'.format('NAZWA WYDAWNICTWA'), '{:<10s}'.format('KRAJ'), '{:<10s}'.format('MIASTO'))
            print(dash)
            for x, y, z in mycursor:
                print('{:<20s}'.format(x), '{:<10s}'.format(y), '{:<10s}'.format(z))
            print(dash)
            confirm = input(f'Czy na pewno chcesz usunąć [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM {wydawnictwa} WHERE {nazwa_wydawnictwa.lower()}="{answer.lower()}"'
                mycursor.execute(query)
                mydb.commit()
                input('Usunięto z Bazy!')
            else:
                input('Anulowano...')
        except:
            input('Coś poszło nie tak...')
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_wydawnictwa()
    menu_wydawnictwa()


def menu_gatunki():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Gatunki\n')
    print('1. Wyświetl')
    print('2. Wyszukaj')
    print('3. Dodaj')
    print('4. Usuń')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        print_gatunek()
        input('Press any key to continue...')
    elif choice == '2':
        os.system('cls')
        user_input = input('Wpisz nazwę szukanego gatunku: ')
        query = f'SELECT * FROM {gatunki} WHERE {nazwa_gatunku} like "%{user_input}%"'
        mycursor.execute(query)
        print(dash)
        print('{:<15s}'.format('NAZWA GATUNKU'))
        print(dash)
        for x in mycursor:
            print(x[0])
        print(dash)
        input('Press any key to continue...')
    elif choice == '3':
        os.system('cls')
        print('Dodawanie nowego gatunku\n')
        nazwa = input('Podaj nazwę gatunku:\n')
        try:
            query = f'INSERT INTO {gatunki} ({nazwa_gatunku}) VALUES ("{nazwa}")'
            mycursor.execute(query)
            mydb.commit()
            input('Dodano!')
        except:
            input('Nie dodano, something went wrong...')
            menu_gatunki()
    elif choice == '4':
        try:
            os.system('cls')
            answer = input('Podaj nazwę gatunku, który chcesz usunąć: ')
            query = f'SELECT * FROM {gatunki} WHERE {nazwa_gatunku.lower()}="{answer.lower()}"'
            mycursor.execute(query)
            print(dash)
            print('{:<15s}'.format('NAZWA GATUNKU'))
            print(dash)
            for x in mycursor:
                print(x[0])
            print(dash)
            confirm = input(f'Czy na pewno chcesz usunąć [Y/N]: ')
            if confirm.lower() == 'y':
                query = f'DELETE FROM {gatunki} WHERE {nazwa_gatunku.lower()}="{answer.lower()}"'
                mycursor.execute(query)
                mydb.commit()
                input('Usunięto z Bazy!')
            else:
                input('Anulowano...')
        except:
            input('Coś poszło nie tak...')
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_gatunki()
    menu_gatunki()


def menu_wyszukaj():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Wyszukaj\n')
    print('Wybierz czego szukasz: \n')
    print('1. Autorzy')
    print('2. Książki')
    print('3. Czytelnicy')
    print('4. Wypożyczenia')
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
            menu_wyszukaj()
        elif choice.lower() == 'exit':
            menu_wyszukaj()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_wyszukaj()
    elif choice == '2':
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nMenu - Wyszukaj - Książki\n')
        print('Wybierz kryterium szukania: \n')
        print('1. Imie lub nazwisko autora')
        print('2. Wydawnictwo')
        print('3. Gatunek')
        print('4. Tytuł')
        print('5. Dostępność')
        print('\nE. Exit\n')
        choice = input('Option: ')
        if choice == '1':
            os.system('cls')
            answer = input('Podaj Imię lub Nazwisko autora: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {imie_autora.lower()} LIKE "%{answer.lower()}%" OR autorzy.nazwisko LIKE "%{answer}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            input('Press any key to continue...')
        elif choice == '2':
            os.system('cls')
            answer = input('Podaj wydawnictwo: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {wydawnictwo_ksiazki.lower()} LIKE "%{answer.lower()}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            input('Press any key to continue...')
        elif choice == '3':
            os.system('cls')
            answer = input('Podaj gatunek: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {gatunek_ksiazki.lower()} LIKE "%{answer.lower()}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            input('Press any key to continue...')
        elif choice == '4':
            os.system('cls')
            answer = input('Podaj tytuł książki: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {tytul_ksiazki.lower()} LIKE "%{answer.lower()}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            input('Press any key to continue...')
        elif choice == '5':
            os.system('cls')
            print('Wybierz dostępne książki: ')
            print('1. TAK')
            print('2. NIE')
            choice = input('Option: ')
            if choice == '1':
                query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {dostepna_ksiazki.lower()} LIKE "%TAK%"'
                mycursor.execute(query)
                print(dash)
                print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                      '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
                print(dash)
                for x, y, z, a, b, c, d in mycursor:
                    print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                          '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
                print(dash)
            else:
                query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE {dostepna_ksiazki.lower()} LIKE "%NIE%"'
                mycursor.execute(query)
                print(dash)
                print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                      '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
                print(dash)
                for x, y, z, a, b, c, d in mycursor:
                    print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                          '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
                print(dash)
            input('Press any key to continue...')
        elif choice.lower() == 'e':
            menu_wyszukaj()
        elif choice.lower() == 'exit':
            menu_wyszukaj()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_wyszukaj()
        menu_wyszukaj()
    elif choice == '3':
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nMenu - Wyszukaj - Czytelnicy\n')
        print('Wybierz kryterium szukania: \n')
        print('1. Imie lub nazwisko')
        print('2. Miejscowość')
        print('3. Adres')
        print('\nE. Exit')
        choice = input('\nOption: ')
        if choice == '1':
            os.system('cls')
            user_input = input('Wpisz imię lub nazwisko czytelnika: ')
            query = f'SELECT * FROM {czytelnicy} WHERE {imie_czytelnika} like "%{user_input}%" or {nazwisko_czytelnika} like "%{user_input}%"'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
                  '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:^15s}'.format('L. KSIĄŻEK'))
            print(dash)
            for x, y, z, a, b, c in mycursor:
                print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:^15d}'.format(c))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice == '2':
            os.system('cls')
            user_input = input('Wpisz miasto czytelnika: ')
            query = f'SELECT * FROM {czytelnicy} WHERE {miasto_czytelnika} like "%{user_input}%"'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
                  '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:^15s}'.format('L. KSIĄŻEK'))
            print(dash)
            for x, y, z, a, b, c in mycursor:
                print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:^15d}'.format(c))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice == '3':
            os.system('cls')
            user_input = input('Wpisz adres[ulica] czytelnika: ')
            query = f'SELECT * FROM {czytelnicy} WHERE {ulica_czytelnika} like "%{user_input}%"'
            mycursor.execute(query)
            print(dash)
            print('{:<4s}'.format('ID'), '{:<15s}'.format('IMIE'), '{:<15s}'.format('NAZWISKO'),
                  '{:<15s}'.format('MIASTO'), '{:<15s}'.format('ULICA'), '{:^15s}'.format('L. KSIĄŻEK'))
            print(dash)
            for x, y, z, a, b, c in mycursor:
                print('{:<4d}'.format(x), '{:<15s}'.format(y), '{:<15s}'.format(z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:^15d}'.format(c))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice.lower() == 'e':
            menu_wyszukaj()
        elif choice.lower() == 'exit':
            menu_wyszukaj()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_wyszukaj()
    elif choice == '4':
        os.system('cls')
        print('BIBLIOTEKARZ (Beta)')
        print('\nMenu - Wyszukaj - Wypożyczenia\n')
        print('Wybierz kryterium szukania: \n')
        print('1. Wypożyczone książki')
        print('2. Książki czytelnika')
        print('3. Wypożyczone dnia')
        print('4. Oddane dnia')
        print('\nE. Exit')
        choice = input('\nOption: ')
        if choice == '1':
            os.system('cls')
            print('Lista aktualnie wypożyczonych książek\n')
            query = f'SELECT wypozyczenia.id_wypozyczenia, czytelnicy.imie, czytelnicy.nazwisko, autorzy.imie, autorzy.nazwisko, ksiazki.tytul, wypozyczenia.data_wypozyczenia, wypozyczenia.data_zwrotu, wypozyczenia.status FROM {wypozyczenia} INNER JOIN {czytelnicy} ON czytelnicy.id_czytelnika=wypozyczenia.id_czytelnika INNER JOIN {ksiazki} ON ksiazki.id_ksiazki=wypozyczenia.id_ksiazki JOIN {autorzy} ON autorzy.id_autora=ksiazki.id_autora'
            mycursor.execute(query)
            print(dash)
            print('{:^4s}'.format('ID'), '{:<20s}'.format('CZYTELNIK'),
                  '{:<20s}'.format('AUTOR'), '{:<15s}'.format('TYTUŁ'), '{:<15s}'.format('OD'), '{:<15s}'.format('DO'), '{:<15s}'.format('STATUS'))
            print(dash)
            for x, y, z, a, b, c, d, e, f in mycursor:
                print('{:^4d}'.format(x), '{:<20s}'.format(y+' '+z), '{:<20s}'.format(a+' '+b), '{:.15s}'.format(c), '{:<15s}'.format(d.strftime('%Y-%m-%d')), '{:<15s}'.format(e.strftime('%Y-%m-%d')), '{:<15s}'.format(f))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice == '2':
            os.system('cls')
            answer = input('Wprowadź imię lub nazwisko czytelnika, którego wypożyczenia chcesz wyświetlić: ')
            query = f'SELECT wypozyczenia.id_wypozyczenia, czytelnicy.imie, czytelnicy.nazwisko, autorzy.imie, autorzy.nazwisko, ksiazki.tytul, wypozyczenia.data_wypozyczenia, wypozyczenia.data_zwrotu, wypozyczenia.status FROM {wypozyczenia} INNER JOIN {czytelnicy} ON czytelnicy.id_czytelnika=wypozyczenia.id_czytelnika INNER JOIN {ksiazki} ON ksiazki.id_ksiazki=wypozyczenia.id_ksiazki JOIN {autorzy} ON autorzy.id_autora=ksiazki.id_autora WHERE czytelnicy.imie like "%{answer}%" OR czytelnicy.nazwisko like "%{answer}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^4s}'.format('ID'), '{:<20s}'.format('CZYTELNIK'),
                  '{:<20s}'.format('AUTOR'), '{:<15s}'.format('TYTUŁ'), '{:<15s}'.format('OD'), '{:<15s}'.format('DO'), '{:<15s}'.format('STATUS'))
            print(dash)
            for x, y, z, a, b, c, d, e, f in mycursor:
                print('{:^4d}'.format(x), '{:<20s}'.format(y+' '+z), '{:<20s}'.format(a+' '+b), '{:.15s}'.format(c), '{:<15s}'.format(d.strftime('%Y-%m-%d')), '{:<15s}'.format(e.strftime('%Y-%m-%d')), '{:<15s}'.format(f))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice == '3':
            os.system('cls')
            answer = input('Podaj datę wypożyczenia [YYYY-MM-DD]: ')
            query = f'SELECT wypozyczenia.id_wypozyczenia, czytelnicy.imie, czytelnicy.nazwisko, autorzy.imie, autorzy.nazwisko, ksiazki.tytul, wypozyczenia.data_wypozyczenia, wypozyczenia.data_zwrotu, wypozyczenia.status FROM {wypozyczenia} INNER JOIN {czytelnicy} ON czytelnicy.id_czytelnika=wypozyczenia.id_czytelnika INNER JOIN {ksiazki} ON ksiazki.id_ksiazki=wypozyczenia.id_ksiazki JOIN {autorzy} ON autorzy.id_autora=ksiazki.id_autora WHERE wypozyczenia.data_wypozyczenia like "%{answer}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^4s}'.format('ID'), '{:<20s}'.format('CZYTELNIK'),
                  '{:<20s}'.format('AUTOR'), '{:<15s}'.format('TYTUŁ'), '{:<15s}'.format('OD'), '{:<15s}'.format('DO'), '{:<15s}'.format('STATUS'))
            print(dash)
            for x, y, z, a, b, c, d, e, f in mycursor:
                print('{:^4d}'.format(x), '{:<20s}'.format(y+' '+z), '{:<20s}'.format(a+' '+b), '{:.15s}'.format(c), '{:<15s}'.format(d.strftime('%Y-%m-%d')), '{:<15s}'.format(e.strftime('%Y-%m-%d')), '{:<15s}'.format(f))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice == '4':
            os.system('cls')
            answer = input('Podaj datę zwrotu [YYYY-MM-DD]: ')
            query = f'SELECT wypozyczenia.id_wypozyczenia, czytelnicy.imie, czytelnicy.nazwisko, autorzy.imie, autorzy.nazwisko, ksiazki.tytul, wypozyczenia.data_wypozyczenia, wypozyczenia.data_zwrotu, wypozyczenia.status FROM {wypozyczenia} INNER JOIN {czytelnicy} ON czytelnicy.id_czytelnika=wypozyczenia.id_czytelnika INNER JOIN {ksiazki} ON ksiazki.id_ksiazki=wypozyczenia.id_ksiazki JOIN {autorzy} ON autorzy.id_autora=ksiazki.id_autora WHERE wypozyczenia.data_wypozyczenia like "%{answer}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^4s}'.format('ID'), '{:<20s}'.format('CZYTELNIK'),
                  '{:<20s}'.format('AUTOR'), '{:<15s}'.format('TYTUŁ'), '{:<15s}'.format('OD'), '{:<15s}'.format('DO'), '{:<15s}'.format('STATUS'))
            print(dash)
            for x, y, z, a, b, c, d, e, f in mycursor:
                print('{:^4d}'.format(x), '{:<20s}'.format(y+' '+z), '{:<20s}'.format(a+' '+b), '{:.15s}'.format(c), '{:<15s}'.format(d.strftime('%Y-%m-%d')), '{:<15s}'.format(e.strftime('%Y-%m-%d')), '{:<15s}'.format(f))
            print(dash)
            input('Press any key to continue...')
            menu_wyszukaj()
        elif choice.lower() == 'e':
            menu_wyszukaj()
        elif choice.lower() == 'exit':
            menu_wyszukaj()
        else:
            input('\nWrong input...')
            os.system('cls')
            menu_wyszukaj()
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        menu_wyszukaj()
    menu_wyszukaj()


def menu_sprawdz_dostepnosc():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Sprawdź dostępność\n')
    user_input = input('Wprowadź imię lub nazwisko autora lub tytuł książki: ')
    os.system('cls')
    query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE (autorzy.imie like "%{user_input}%" OR autorzy.nazwisko like "%{user_input}%" OR ksiazki.tytul like "%{user_input}%") AND {dostepna_ksiazki} LIKE "%TAK%"'
    mycursor.execute(query)
    print(dash)
    print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
          '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
    print(dash)
    for x, y, z, a, b, c, d in mycursor:
        print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
              '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
    print(dash)
    input('\nPress any key to continue...')
    main_menu()


def menu_zmien_status():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Zmień status\n')
    print('1. Książki')
    print('2. Wypożyczenia')
    print('\nE. Exit')
    choice = input('\nOption: ')
    if choice == '1':
        os.system('cls')
        user_input = input('Wprowadź tytuł książki aby wyszukać lub zostaw puste aby wyświetlić wszystkie: ')
        if user_input == '':
            os.system('cls')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            answer = input('Podaj ID książki, której status chcesz zmienić: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE id_ksiazki="{answer}"'
            mycursor.execute(query)
            for x, y, z, a, b, c, d in mycursor:
                print(x, y, z, '{:.10s}'.format(c))
            nowy_status = input(f'Wprowadź nowy status dla ID-{x} [TAK/NIE]: ')
            if nowy_status.lower() == 'tak' or nowy_status.lower() == 't':
                query = f'UPDATE ksiazki SET dostepna="TAK" where id_ksiazki="{x}"'
                mycursor.execute(query)
                mydb.commit()
                input('Status zmieniony na "TAK"')
            elif nowy_status.lower() == 'nie' or nowy_status.lower() == 'n':
                query = f'UPDATE ksiazki SET dostepna="NIE" where id_ksiazki="{x}"'
                mycursor.execute(query)
                mydb.commit()
                input('Status zmieniony na "NIE"')
            else:
                input('Coś poszło nie tak...')
                main_menu()
            main_menu()
        elif user_input is not '':
            os.system('cls')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE ksiazki.tytul LIKE "%{user_input}%"'
            mycursor.execute(query)
            print(dash)
            print('{:^5s}'.format('ID'), '{:<25s}'.format('AUTOR'), '{:<15s}'.format('WYDAWNICTWO'),
                  '{:<15s}'.format('GATUNEK'), '{:<40s}'.format('TYTUŁ'), '{:^5s}'.format('DOSTĘPNA'))
            print(dash)
            for x, y, z, a, b, c, d in mycursor:
                print('{:^5d}'.format(x), '{:<25s}'.format(y + ' ' + z), '{:<15s}'.format(a),
                      '{:<15s}'.format(b), '{:<40s}'.format(c), '{:^5s}'.format(d))
            print(dash)
            answer = input('Podaj ID książki, której status chcesz zmienić: ')
            query = f'SELECT ksiazki.id_ksiazki, autorzy.imie, autorzy.nazwisko, ksiazki.wydawnictwo, ksiazki.gatunek, ksiazki.tytul, ksiazki.dostepna FROM {ksiazki} INNER JOIN {autorzy} ON ksiazki.id_autora=autorzy.id_autora WHERE id_ksiazki="{answer}"'
            mycursor.execute(query)
            for x, y, z, a, b, c, d in mycursor:
                print(x, y, z, '{:.10s}'.format(c))
            nowy_status = input(f'Wprowadź nowy status dla ID-{x} [TAK/NIE]: ')
            if nowy_status.lower() == 'tak' or nowy_status.lower() == 't':
                query = f'UPDATE ksiazki SET dostepna="TAK" where id_ksiazki="{x}"'
                mycursor.execute(query)
                mydb.commit()
                input('Status zmieniony na "TAK"')
            elif nowy_status.lower() == 'nie' or nowy_status.lower() == 'n':
                query = f'UPDATE ksiazki SET dostepna="NIE" where id_ksiazki="{x}"'
                mycursor.execute(query)
                mydb.commit()
                input('Status zmieniony na "NIE"')
            else:
                input('Coś poszło nie tak...')
                main_menu()
            main_menu()
    elif choice == '2':
        os.system('cls')
        query = f'SELECT * FROM {wypozyczenia}'
        mycursor.execute(query)
        print(dash)
        print('{:^4s}'.format('ID'), '{:^10s}'.format('ID KSIĄŻKI'), '{:^15s}'.format('ID CZYTELNIKA'),
              '{:<20s}'.format('DATA ZAMÓWIENIA'), '{:<20s}'.format('DATA WYPOŻYCZENIA'),
              '{:<20s}'.format('DATA ZWROTU'), '{:<15s}'.format('STATUS'))
        print(dash)
        for x, y, z, a, b, c, d in mycursor:
            print('{:^4d}'.format(x), '{:^10d}'.format(y), '{:^15d}'.format(z), '{:<20}'.format(a.strftime('%Y-%m-%d')),
                  '{:<20s}'.format(b.strftime('%Y-%m-%d')), '{:<20s}'.format(c.strftime('%Y-%m-%d')),
                  '{:<15}'.format(d))
        print(dash)
        user_input = input('\nWprowadź ID wypożyczenia, którego status chcesz zmienić: ')
        query = f'SELECT * FROM {wypozyczenia} WHERE id_wypozyczenia="{user_input}"'
        mycursor.execute(query)
        for x, y, z, a, b, c, d in mycursor:
            print('{:^4d}'.format(x), '{:^10d}'.format(y), '{:^15d}'.format(z), '{:<20}'.format(a.strftime('%Y-%m-%d')),
                  '{:<20s}'.format(b.strftime('%Y-%m-%d')), '{:<20s}'.format(c.strftime('%Y-%m-%d')),
                  '{:<15}'.format(d))
        answer = input('Wprowadź nowy status: ')
        query = f'UPDATE wypozyczenia SET status="{answer}" WHERE id_wypozyczenia="{x}"'
        mycursor.execute(query)
        mydb.commit()
        input('Zmieniono status!')
        main_menu()
    elif choice.lower() == 'e':
        main_menu()
    elif choice.lower() == 'exit':
        main_menu()
    else:
        input('\nWrong input...')
        os.system('cls')
        main_menu()
    main_menu()


def menu_custom():
    os.system('cls')
    print('BIBLIOTEKARZ (Beta)')
    print('\nMenu - Custom (Zaawansowany)\n')
    print('Nie znalazłeś czego szukasz?\n')
    user_input = input('Wprowadź własne zapytanie SQL: ')
    os.system('cls')
    query = f'{user_input}'
    # query = f'select autorzy.imie, autorzy.nazwisko, ksiazki.tytul from autorzy inner join ksiazki on ksiazki.id_autora=autorzy.id_autora'
    mycursor.execute(query)
    print(dash)
    for x in mycursor:
        print(x)
    print(dash)
    input('\nPress any key to continue...')
    main_menu()


main_menu()
