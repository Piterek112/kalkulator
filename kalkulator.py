import time
import math

def zapisz_do_pliku(historia_obliczen):
    with open("historia_obliczen.txt", "a") as plik:
        for obliczenie in historia_obliczen:
            plik.write(obliczenie + "\n")

def wczytaj_historie_z_pliku():
    historia_z_pliku = []
    try:
        with open("historia_obliczen.txt", "r") as plik:
            historia_z_pliku = plik.readlines()
    except FileNotFoundError:
        print("Plik z historią nie istnieje.")
    return historia_z_pliku

def kalkulator_podstawowy(historia_obliczen):
    
    start = True
    while start:

        print("Wybierz operację:")
        print("Dodawanie")
        print("Odejmowanie")
        print("Mnożenie")
        print("Dzielenie")
        print("Potęgowanie")
        print("1. Wczytaj historię obliczeń z pliku")
        print("2. Wyświetl historię obliczeń")
        print("3. Zapisz historię obliczeń do pliku")
        x = input("Co chcesz zrobić? ")
        if x.lower() == 'dodawanie':
            dodawanie1 = int(input("Daj mi liczbe "))
            dodawanie2 = int(input("Daj mi drugą liczbe do dodawania "))
            koniec_dodawania = dodawanie1 + dodawanie2
            obliczenie = f"Dodawanie: {dodawanie1} + {dodawanie2} = {koniec_dodawania}"
            print(f"Wynik to {koniec_dodawania}")
            historia_obliczen.append(obliczenie)
            time.sleep(0.3)
            start_dodawanie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
            if start_dodawanie.lower() == 'tak':
                start = True
            elif start_dodawanie.lower() == 'nie':
                start = False
                print("Do zobaczenia!")
        elif x.lower() == 'odejmowanie':
            odejmowanie1 = int(input("Podaj liczbe "))
            odejmowanie2 = int(input("Podaj liczbę którą chcesz odjąć "))
            koniec_odejmowania = odejmowanie1 - odejmowanie2
            obliczenie = f"Odejmowanie: {odejmowanie1} - {odejmowanie2} = {koniec_odejmowania}"
            print(f"Wynik to {koniec_odejmowania}")
            historia_obliczen.append(obliczenie)
            time.sleep(0.3)
            start_odejmowanie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
            if start_odejmowanie.lower() == 'tak':
                start = True
            elif start_odejmowanie.lower() == 'nie':
                start = False
                print("Do zobaczenia")
        elif x.lower() == 'mnożenie':
            mnozenie1 = int(input("Podaj liczbe "))
            mnozenie2 = int(input("Podaj mnożnik "))
            koniec_mnozenia = mnozenie1 * mnozenie2
            obliczenie = f"Mnożenie: {mnozenie1} * {mnozenie2} = {koniec_mnozenia}"
            print(f"Wynik mnożenia to {koniec_mnozenia}")
            historia_obliczen.append(obliczenie)
            time.sleep(0.3)
            start_mnozenie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
            if start_mnozenie.lower() == 'tak':
                start = True
            elif start_mnozenie.lower() == 'nie':
                start = False
                print("Do zobaczenia")
        elif x.lower() == 'dzielenie':
            dzielenie1 = int(input("Podaj liczbe "))
            dzielenie2 = int(input("Podaj dzielnik "))
            if dzielenie2 != 0:
                koniec_dzielenia = dzielenie1 / dzielenie2
                obliczenie = f"Dzielenie: {dzielenie1} / {dzielenie2} = {koniec_dzielenia}"
                print(f"Wynik to {koniec_dzielenia}")
                historia_obliczen.append(obliczenie)
            else:
                print("Błąd: Dzielenie przez zero.")
            time.sleep(0.3)
            start_dzielenia = input("Czy chcesz zacząć od nowa? Tak/Nie ")
            if start_dzielenia.lower() == 'tak':
                start = True
            elif start_dzielenia.lower() == 'nie':
                start = False
                print("Do zobaczenia")
        elif x.lower() == 'potegowanie':
            potegowanie1 = int(input("Podaj liczbe "))
            potegowanie2 = int(input("Do której potęgi chcesz podnieść liczbe? "))
            koniec_potegowania = potegowanie1 ** potegowanie2
            obliczenie = f"Potęgowanie: {potegowanie1} ^ {potegowanie2} = {koniec_potegowania}"
            print(f"Wynik to {koniec_potegowania}")
            historia_obliczen.append(obliczenie)
            time.sleep(0.3)
            start_potegowania = input("Czy chesz zacząć od nowa? Tak / Nie ")
            if start_potegowania.lower() == 'tak':
                start = True
            elif start_potegowania.lower() == 'nie':
                start = False
                print("Do zobaczenia")
        elif x == '1':
            wczytana_historia = wczytaj_historie_z_pliku()
            if wczytana_historia:
                print("Wczytana historia obliczeń z pliku:")
                for obliczenie in wczytana_historia:
                    print(obliczenie.strip())
            else:
                print("Plik z historią jest pusty lub nie istnieje.")
        elif x == '2':
            print("Historia obliczeń:")
            for obliczenie in historia_obliczen:
                print(obliczenie)
        elif x == '3':
            zapisz_do_pliku(historia_obliczen)
            print("Historia obliczeń została zapisana do pliku 'historia_obliczen.txt'.")
        else:
            print("Błąd - niepoprawna operacja")
            start = True

def kalkulator_logarytmow(historia_obliczen):
    start2 = True
    while start2:

        print("Witaj w kalkulatorze logarytmów")
        print("1. Logarytm naturalny (ln)")
        print("2. Logarytm o dowolnej podstawie")
        print("3. Wczytaj historię obliczeń z pliku")
        print("4. Wyświetl historię obliczeń")
        print("5. Zapisz historię obliczeń do pliku")
        time.sleep(0.3)
        wybor = input("Wybierz opcję (1 / 2 / 3 / 4 / 5): ")
        if wybor == '1':
            liczba = float(input("Podaj liczbę, której logarytm naturalny chcesz obliczyć: "))      
            if liczba > 0:
                ln = True
                while ln:
                    wynik = math.log(liczba)
                    obliczenie = f"Ln {liczba} = {wynik}"
                    print(obliczenie)
                    historia_obliczen.append(obliczenie)
                    od_nowa_log = input("Czy chcesz zacząć od nowa? Tak/Nie ")
                    if od_nowa_log.lower() == 'tak':
                        start2 = True
                        ln = False
                    elif od_nowa_log.lower() == 'nie':
                        print("Do zobaczenia")
                        start2 = False
                        ln = False
                        zapisz_do_pliku(historia_obliczen)
                        break
                else:
                    print("Błąd: Liczba musi być większa niż 0")
                    ln = True
        elif wybor == '2':
            dp = True
            while dp:
                liczba = float(input("Podaj liczbę: "))
                podstawa = float(input("Podaj podstawę logarytmu: "))
                if liczba > 0 and podstawa > 0 and podstawa != 1:
                    wynik = math.log(liczba, podstawa)
                    obliczenie = f"Log{podstawa}{liczba} = {wynik}"
                    print(obliczenie)
                    historia_obliczen.append(obliczenie)
                    od_nowa_pd = input("Czy chcesz zacząć od nowa? Tak/Nie ")
                    if od_nowa_pd.lower() == 'tak':
                        start2 = True
                        dp = False
                    elif od_nowa_pd.lower() == 'nie':
                        print("Do zobaczenia")
                        start2 = False
                        dp = False
                        zapisz_do_pliku(historia_obliczen)
                        break
                else:
                    print("Błąd: Liczba i podstawa muszą być większe od zera, a podstawa nie może być równa 1.")
                    dp = True
        elif wybor == '3':
            wczytana_historia = wczytaj_historie_z_pliku()
            if wczytana_historia:
                print("Wczytana historia obliczeń z pliku:")
                for obliczenie in wczytana_historia:
                    print(obliczenie.strip())
            else:
                print("Plik z historią jest pusty lub nie istnieje.")
        elif wybor == '4':
            print("Historia obliczeń:")
            for obliczenie in historia_obliczen:
                print(obliczenie)
        elif wybor == '5':
            zapisz_do_pliku(historia_obliczen)
            print("Historia obliczeń została zapisana do pliku 'historia_obliczen.txt'.")
        else:
            time.sleep(1)
            print("Błąd: Wybierz poprawną opcję (1, 2, 3, 4 lub 5).")
            print("\n")

historia_obliczen = []
print("Witaj w kalkulatorze!")
print("Kiedy chcesz wybrać:")
print("1 - Kalkulator podstawowy")
print("2 - Kalkulator logarytmów")
print("3 - Wczytaj historię obliczeń")
wybor_pierwszy = input("Wybierz opcję (1 / 2 / 3): ")
wybor_pierwszy = int(wybor_pierwszy)
if wybor_pierwszy == 1:
    kalkulator_podstawowy(historia_obliczen)
elif wybor_pierwszy == 2:
    kalkulator_logarytmow(historia_obliczen)
elif wybor_pierwszy == 3:
    wczytana_historia = wczytaj_historie_z_pliku()
    if wczytana_historia:
        print("Wczytana historia obliczeń z pliku:")
        for obliczenie in wczytana_historia:
            print(obliczenie.strip())
    else:
        print("Plik z historią jest pusty lub nie istnieje.")
else:
    print("Błąd")
