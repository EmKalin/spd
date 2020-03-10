import os


def pobierz_dane(plik):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plik):  # sprawdzamy czy plik istnieje na dysku
        with open(plik, "r") as zawartosc:  # otwieramy plik do odczytu
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                #linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
                # dodajemy elementy do tupli a tuplę do listy
                dane.append(tuple(map(int,linia.split(" "))))
    else:
        print("Plik z danymi", plikcsv, "nie istnieje!")
    return tuple(dane) # przekształcamy listę na tuplę i zwracamy ją

def calculate(tablica,n):
    S=[]
    S.append(tablica[0][0])
    C=[]
    C.append(S[0]+tablica[0][1])
    Cmax=C[0]+tablica[0][2]
    for i in range (1,n):
        S.append(max(tablica[i][0],C[i-1]))
        C.append(S[i]+tablica[i][1])
        Cmax=max(Cmax,C[i]+tablica[i][2])

    return Cmax
pliki=["data10.txt","data20.txt","data50.txt","data100.txt","data200.txt","data500.txt"]
for j in range (0,6):
    dane=pobierz_dane(pliki[j])
    #print(dane)
    n=dane[0][0]
    r=dane[0][1]
    #print(n)
    dane=list(dane[1:n+1])
    #print(dane)
    wynik=calculate(dane,n)
    print("Nazwa pliku: ",pliki[j])
    print("Wynik nieposortowany:",wynik)
    dane.sort(key=lambda x: x[0])
    wynik=calculate(dane,n)
    print("Wynik posortowany:",wynik)