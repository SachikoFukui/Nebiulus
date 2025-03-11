import os
import random
import msvcrt 
GraczGra = True
KrupierGra = True

os.system('cls' if os.name == 'nt' else 'clear')

# Karty
stosKart = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A']

rekaGracza = []
rekaKrupiera = []

# Rozdawanie kart

def Rozdaj(turn):
    karta = random.choice(stosKart)
    turn.append(karta)
    stosKart.remove(karta)

# Zliczanie kart

def Zliczenie(reka):
    wynik = 0
    asy = 0
    for karta in reka:
        if karta in range(11):
            wynik += karta
        elif karta in ['J', 'K', 'Q']:
            wynik += 10
        else:
            wynik += 11
            asy += 1
    while asy and wynik > 21:
        wynik -= 10
        asy -= 1
    return wynik

# Szukanie zwyciezcy
def PokazRekeKrupiera():
    if len(rekaKrupiera) == 2:
        return rekaKrupiera[0]
    elif len(rekaKrupiera) > 2:
        return rekaKrupiera[0], rekaKrupiera[1]
    

# Petla gry
for _ in range(2):
    Rozdaj(rekaGracza)
    Rozdaj(rekaKrupiera)

while GraczGra or KrupierGra:
    print(f"Krupier ma: {PokazRekeKrupiera()}, ?")
    print(f"Masz: {rekaGracza}, co daje {Zliczenie(rekaGracza)}")
    if GraczGra:
        ciągnieCzyNieCiągnie = input("1:Zostaw\n2:Ciągnij\n")
    if Zliczenie(rekaKrupiera) > 16:
        KrupierGra = False
    else:
        Rozdaj(rekaKrupiera)
    
    if ciągnieCzyNieCiągnie == "1":
        GraczGra = False
    elif ciągnieCzyNieCiągnie == "2":
        Rozdaj(rekaGracza)

    if Zliczenie(rekaGracza) >= 21:
        break
    elif Zliczenie(rekaKrupiera) >=21:
        break

# Koncowe wyniki
if Zliczenie(rekaGracza) == 21:
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("BLACKJACK! Wygrałeś!")
elif Zliczenie(rekaKrupiera) == 21:
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("BLACKJACK! Przegrałeś!")
elif Zliczenie(rekaGracza) > 21:
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("FURA! Przegrałeś!")
elif Zliczenie(rekaKrupiera) > 21:
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("FURA! Wygrałeś!")

elif 21 - Zliczenie(rekaKrupiera) < 21 - Zliczenie(rekaGracza):
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("Krupier wygrywa!")
elif 21 - Zliczenie(rekaKrupiera) > 21 - Zliczenie(rekaGracza):
    print(f"Masz {rekaGracza}, co daje {Zliczenie(rekaGracza)}\nKrupier ma {rekaKrupiera}, co daje mu {Zliczenie(rekaKrupiera)}\n")
    print("Wygrywasz!")

print("\nNaciśnij dowolny klawisz, aby kontynuować...")
key = msvcrt.getch() 