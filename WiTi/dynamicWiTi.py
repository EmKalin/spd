import os
import math
import copy
import heapq
import itertools
from typing import List, Any, Union


def pobierz_dane(plik):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plik):  # sprawdzamy czy plik istnieje na dysku
        with open(plik, "r") as zawartosc:  # otwieramy plik do odczytu
            i = 0
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                x = map(int, linia.split(" "))   # dodajemy elementy do tupli a tuplę do listy
                x = list(x)                      # tutaj takie wygibasy żeby dodać czwarta liczbę
                x.append(i)                      # która jest kolejnością zadań
                dane.append(list(x))            # pewnie da się ładniej ale jestem nowy w Python
                i = i + 1                        # i++ zadania są numerowane od 1 do n
    else:
        print("Plik z danymi", plik, "nie istnieje!")
    return list(dane)  # przekształcamy listę na tuplę i zwracamy ją


def kolejnosc(lista):
    y = []
    for item in lista:
        y.append(item[3])
    return y


def dynamicW(tablica):
    C = 0
   # x=bin(2**10-1)

    # print(x[2:])

   # n = len(tablica)

    for i in range(0, len(tablica)):
        C = C+tablica[i][0]


    fin=[]

    for j in range(0, len(tablica)):

        G = copy.deepcopy(tablica)
        K = G[j][1]*max(C-G[j][2], 0)

        if len(G)>1:
            G.pop(j)
            fin.append(dynamicW(G)+K)
        else:
            fin.append(K)

    opt = min(fin)

    return opt



def zad2(pliki):

    dane = pobierz_dane(pliki)
    n = dane[0][0]
    r = dane[0][1]
    dane = list(dane[1:n + 1])
    wynik = dynamicW(dane)
    print("Nazwa pliku: ", pliki)
    print("Wynik: ", wynik)

zad2("data13.txt")