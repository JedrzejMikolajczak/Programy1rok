def wczytaj_graf(nazwa_pliku):
    plik = open(nazwa_pliku, "r")
    linie = plik.readlines()
    plik.close()
    n, m = map(int, linie[0].split())
    krawedzie = []
    for i in range(1, m + 1):
        u, v = map(int, linie[i].split())
        krawedzie.append((u, v))
    macierz_sasiedztwa = [[0] * (n + 1) for _ in range(n + 1)]
    lista_nastepnikow = [[] for _ in range(n + 1)]
    for u, v in krawedzie:
        macierz_sasiedztwa[u][v] = 1
        lista_nastepnikow[u].append(v)
    return n, macierz_sasiedztwa, lista_nastepnikow

def Kahn_ms(n, macierz):
    stopien_wej = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if macierz[u][v] == 1:
                stopien_wej[v] += 1

    kolejka = []
    for u in range(1, n + 1):
        if stopien_wej[u] == 0:
            kolejka.append(u)
    kolejka.sort()

    wynik = []
    while kolejka:
        u = kolejka.pop(0)
        wynik.append(u)
        nowe = []
        for v in range(1, n + 1):
            if macierz[u][v] == 1:
                stopien_wej[v] -= 1
                if stopien_wej[v] == 0:
                    nowe.append(v)
        kolejka.extend(nowe)
        kolejka.sort()

    if len(wynik) != n:
        print("Graf zawiera cykl. Nie można posortować topologicznie.")
    else:
        print("Sortowanie topologiczne (Kahn_ms):", wynik)
def Kahn_ln(n, lista):
    stopien_wej = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in lista[u]:
            stopien_wej[v] += 1
    kolejka = []
    for u in range(1, n + 1):
        if stopien_wej[u] == 0:
            kolejka.append(u)
    kolejka.sort()
    wynik = []
    while kolejka:
        u = kolejka.pop(0)
        wynik.append(u)
        nowe = []
        for v in lista[u]:
            stopien_wej[v] -= 1
            if stopien_wej[v] == 0:
                nowe.append(v)
        kolejka.extend(nowe)
        kolejka.sort()
    if len(wynik) != n:
        print("Graf zawiera cykl. Nie można posortować topologicznie.")
    else:
        print("Sortowanie topologiczne (Kahn_ln):", wynik)

def tarjan_ms(n, macierz_sasiedztwa, start):
    kolory = ['bialy'] * (n + 1)
    wynik = []
    cykl = [False]

    def dfs(u):
        if cykl[0]:
            return
        kolory[u] = 'szary'
        for v in range(1, n + 1):
            if macierz_sasiedztwa[u][v]:
                if kolory[v] == 'bialy':
                    dfs(v)
                elif kolory[v] == 'szary':
                    cykl[0] = True
        kolory[u] = 'czarny'
        wynik.append(u)

    dfs(start)
    for u in range(1,n+1):
        if kolory[u]=='bialy':
            dfs(u)

    if cykl[0]:
        print("Wykryto cykl. Sortowanie jest niemożliwe")
        return []

    return wynik[::-1]
def tarjan_ln(n, lista_nastepnikow, start):
    kolory = ['bialy'] * (n + 1)
    wynik = []
    cykl = [False]

    def dfs(u):
        if cykl[0]:
            return
        kolory[u] = 'szary'
        for v in lista_nastepnikow[u]:
            if kolory[v] == 'bialy':
                dfs(v)
            elif kolory[v] == 'szary':
                cykl[0] = True
        kolory[u] = 'czarny'
        wynik.append(u)
    dfs(start)

    for u in range(1,n+1):
        if kolory[u]=='bialy':
            dfs(u)
    if cykl[0]:
        print("Wykryto cykl. Sortowanie jest niemożliwe")
        return []

    return wynik[::-1]


n, macierz, lista = wczytaj_graf("plik2.txt")

Kahn_ms(n, macierz)
Kahn_ln(n, lista)
start = int(input("Podaj wierzchołek startowy: "))
if not (1 <= start <= n):
    print("Nieprawidłowy indeks wierzchołka.")
else:
    wynik = tarjan_ms(n, macierz, start)
    wynik2 = tarjan_ln(n, lista, start)
    if wynik:
        print("Sortowanie macierz sasiedztwa: ", wynik)
        print("Sortowanie lista nastepnikow: ", wynik2)
