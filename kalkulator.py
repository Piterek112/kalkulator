import time
import math

def kalkulator_podstawowy():
    
    start = True
    while start == True:

        print("Wybierz operację:")
        print("Dodawanie")
        print("Odejmowanie")
        print("Mnożenie")
        print("Dzielenie")
        print("Potegowanie")
        x = input("Co chcesz zrobić? ")
        if x.lower() == 'dodawanie':
            dodawanie1 = int(input("Daj mi liczbe "))
            dodawanie2 = int(input("Daj mi drugą liczbe do dodawania "))
            koniec_dodawania = dodawanie1 + dodawanie2
            print(f"Wynik to {koniec_dodawania}")
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
            print(f"Wynik to {koniec_odejmowania}")
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
            print(f"Wynik mnożenia to {koniec_mnozenia}")
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
            koniec_dzielenia = (dzielenie1 * dzielenie2 **-1)
            print(f"Wynik to {koniec_dzielenia}")
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
            koniec_potegowania = (potegowanie1 ** potegowanie2 )
            print(f"Wynik to {koniec_potegowania}")
            time.sleep(0.3)
            start_potegowania = input("Czy chesz zacząć od nowa? Tak / Nie ")
            if start_potegowania.lower() =='tak':
                start = True
            elif start_potegowania.lower() == 'nie':
                start = False
                print("Do zobaczenia")
        

        else:
            print("Błąd - niepoprawna operacja")
            start = True

def kalkulator_lagorytmow():
    start2 = True
    while start2 == True:
        print("Witaj w kalkulatorze lagorytmów")
        print("1. Logarytm naturalny (ln)")
        print("2. Logarytm o dowolnej podstawie")
        time.sleep(0.3)
        wybor = input("Wybierz opcje (1 / 2) : ")
        if wybor == '1':
            liczba = float(input("Podaj liczbę, której logarytm naturalny chcesz obliczyć: "))      
            if liczba > 0:
                ln = True
                while ln == True:
                    wynik = math.log(liczba)
                    print(f"Ln {liczba} = {wynik}")
                    od_nowa_log = input("Czy chcesz zacząć od nowa? Tak/Nie ")
                    if od_nowa_log.lower() == 'tak':
                        start2 = True
                        ln = False
                    elif od_nowa_log.lower() == 'nie':
                        print("Do zobaczenia ")
                        start2 = False
                        ln = False
                        break
                else:
                    print("Bląd liczba mus być wieksz niż 0")
                    ln = True
                    


        elif wybor =='2':
            dp = True
            while dp == True:
                    liczba = float(input("Podaj liczbe: "))
                    podstawa = float(input("Podaj podstawe lagorytmu: "))
                    if liczba > 0 and podstawa > 0 and podstawa != 1:
                        wynik = math.log(liczba, podstawa)
                        print(f"Log{podstawa}{liczba} = {wynik}")
                        od_nowa_pd = input("Czy chcesz zacząć od nowa? Tak/Nie ")
                        if od_nowa_pd.lower() == 'tak':
                            start2 = True
                            dp = False
                        elif od_nowa_pd.lower() == 'nie':
                            print("Do zobaczenia")
                            start2 = False
                            ln = False
                            break

                    else:
                        print("Błąd: Liczba i podstawa muszą być większe od zera, a podstawa nie może być równa 1.")
                        dp = True
            
        else:
            time.sleep(1)
            print("Błąd: Wybierz poprawną opcję (1 lub 2).")
            print("\n")
        

print("Witaj w kalkulatorze!")
print("Kiedy chcesz wybrać:\n1-Kalkulator podstawowy\n2-Kalkulator lagorytmów")
wybor_pierwszy = input("1 Czy 2 ")
wybor_pierwszy = int(wybor_pierwszy)
if wybor_pierwszy == 1:
    kalkulator_podstawowy()
elif wybor_pierwszy == 2:
    kalkulator_lagorytmow()
else:
    print("Błąd")




















