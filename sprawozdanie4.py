def wczytaj_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        linie = f.readlines()

    n, m = map(int, linie[0].split())
    macierz = [[0] * n for _ in range(n)]

    for linia in linie[1:]:
        u, v = map(int, linia.split())
        u -= 1
        v -= 1
        macierz[u][v] = 1
        macierz[v][u] = 1
    return macierz

def wczytaj_krawedzie_z_pliku(nazwa_pliku):
    krawedzie = []
    with open(nazwa_pliku, 'r') as plik:
        next(plik)
        for linia in plik:
            linia = linia.strip()
            if linia:
                u, v = map(int, linia.split())
                krawedzie.append([u, v])

    return krawedzie


def stworz_liste_nastepnikow(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        pierwsza_linia = plik.readline().split()
        n = int(pierwsza_linia[0])
        lista_nastepnikow = [[] for _ in range(n + 1)]
        pominiete_cykle = 0
        krawedzie = set()
        cykle_dwu = set()

        for _ in range(int(pierwsza_linia[1])):
            linia = plik.readline().strip()
            if not linia:
                continue
            u, v = map(int, linia.split())
            if u == v:
                pominiete_cykle += 1
                continue
            if (u, v) in cykle_dwu or (v, u) in cykle_dwu:
                continue
            if (v, u) in krawedzie:
                pominiete_cykle += 2
                cykle_dwu.add((u, v))
                cykle_dwu.add((v, u))
                lista_nastepnikow[v].remove(u)
                continue

            krawedzie.add((u, v))
            lista_nastepnikow[u].append(v)
    for i in range(len(lista_nastepnikow)):
        lista_nastepnikow[i].sort()
        if not lista_nastepnikow[i]:
            lista_nastepnikow[i] = [0]

    return lista_nastepnikow

def nastepny_nastepnik(lista_nastepnikow, wierzcholek, aktualny_nastepnik):
    nastepniki = lista_nastepnikow[wierzcholek]
    try:
        indeks = nastepniki.index(aktualny_nastepnik)
    except ValueError:
        return nastepniki[0] if nastepniki else None
    if indeks + 1 < len(nastepniki):
        return nastepniki[indeks + 1]
    else:
        return nastepniki[-1] if nastepniki else None


def stworz_liste_poprzednikow(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        pierwsza_linia = plik.readline().split()
        n = int(pierwsza_linia[0])
        lista_poprzednikow = [[] for _ in range(n + 1)]
        pominiete_cykle = 0
        krawedzie = set()
        cykle_dwu = set()

        for _ in range(int(pierwsza_linia[1])):
            linia = plik.readline().strip()
            if not linia:
                continue
            u, v = map(int, linia.split())

            if u == v:
                pominiete_cykle += 1
                continue

            if (u, v) in cykle_dwu or (v, u) in cykle_dwu:
                continue

            if (v, u) in krawedzie:
                pominiete_cykle += 2
                cykle_dwu.add((u, v))
                cykle_dwu.add((v, u))
                lista_poprzednikow[u].remove(v)
                continue

            krawedzie.add((u, v))
            lista_poprzednikow[v].append(u)

    for i in range(len(lista_poprzednikow)):
        lista_poprzednikow[i].sort()
        if not lista_poprzednikow[i]:
            lista_poprzednikow[i] = [0]

    return lista_poprzednikow


def stworz_liste_braku_incydencji(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        pierwsza_linia = plik.readline().strip().split()
        n = int(pierwsza_linia[0])

        wszystkie_polaczenia = {w: set() for w in range(1, n + 1)}

        for linia in plik:
            linia = linia.strip()
            if linia:
                u, v = map(int, linia.split())
                wszystkie_polaczenia[u].add(v)
                wszystkie_polaczenia[v].add(u)

    wynik = [[]]

    for wierzcholek in range(1, n + 1):
        wszyscy_mozliwi = set(range(1, n + 1)) - {wierzcholek}

        brakujacy = []
        for sasiad in wszyscy_mozliwi:
            if sasiad not in wszystkie_polaczenia[wierzcholek] and wierzcholek not in wszystkie_polaczenia[sasiad]:
                brakujacy.append(sasiad)

        if wierzcholek not in wszystkie_polaczenia[wierzcholek]:
            brakujacy.insert(0, wierzcholek)

        wynik.append(sorted(brakujacy))
    for i in range(len(wynik)):
        if wynik[i] == []:
            wynik[i] = [0]
    return wynik

def znajdz_cykle(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        n, m = map(int, plik.readline().split())

        krawedzie = set()

        petle_wlasne = set()

        cykle_dwu = set()

        for linia in plik:
            linia = linia.strip()
            if linia:
                u, v = map(int, linia.split())
                if u == v:
                    petle_wlasne.add((u, v))
                else:
                    if (v, u) in krawedzie:
                        cykle_dwu.add((u, v))
                        cykle_dwu.add((v, u))
                    krawedzie.add((u, v))
    wynik = []
    for u, v in petle_wlasne:
        wynik.append([u, v])
    for u, v in cykle_dwu:
        wynik.append([u, v])

    return wynik

def wypelnij_konkretna_kolumne(macierz, numer_kolumny, macierz_danych_do_wypelnienia):
    for i in range(1, len(macierz_danych_do_wypelnienia)):
        wartosc = macierz_danych_do_wypelnienia[i][0]
        macierz[i-1][numer_kolumny] = wartosc

    return macierz

def macierz_grafu(liczba_wierzcholkow, nazwa_pliku, krawedzie):
    lista_poprzednikow = stworz_liste_poprzednikow(nazwa_pliku)
    lista_nastepnikow = stworz_liste_nastepnikow(nazwa_pliku)
    lista_bez_polaczen = stworz_liste_braku_incydencji(nazwa_pliku)
    lista_cykli = znajdz_cykle(nazwa_pliku)
    n = liczba_wierzcholkow
    rows = liczba_wierzcholkow
    cols = liczba_wierzcholkow + 4
    macierz_grafu = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    wypelnij_konkretna_kolumne(macierz_grafu,liczba_wierzcholkow+1,lista_nastepnikow)
    for u,v in krawedzie:
        wartosc = nastepny_nastepnik(lista_nastepnikow,u,v)
        macierz_grafu[u-1][v] = wartosc
    wypelnij_konkretna_kolumne(macierz_grafu,liczba_wierzcholkow+2,lista_poprzednikow)
    for v,u in krawedzie:
        wartosc = nastepny_nastepnik(lista_poprzednikow,u,v) + liczba_wierzcholkow
        macierz_grafu[u-1][v] = wartosc
    wypelnij_konkretna_kolumne(macierz_grafu,liczba_wierzcholkow+3,lista_bez_polaczen)
    for i in range(1,len(lista_bez_polaczen)):
        u = i
        for j in range(len(lista_bez_polaczen[i])):
            v = lista_bez_polaczen[i][j]
            wartosc = nastepny_nastepnik(lista_bez_polaczen,u,v)*-1
            macierz_grafu[u-1][v] = wartosc
    for el in lista_cykli:
        a = el[0]
        b = el[1]
        macierz_grafu[a-1][liczba_wierzcholkow+4] = b
        macierz_grafu[a-1][b] = b+2*liczba_wierzcholkow
    return macierz_grafu

#Algorytm Robertsa-Floresa (cykl Hamiltona)
def hamiltonian(v, n, macierz, O, Path, pos, start):
    if pos == n:
        if macierz[v][start] == 1:
            Path[pos] = v
            return True
        else:
            return False
    #przechpdzimy do sasiadow V
    for u in range(n):
        if macierz[v][u] == 1 and not O[u]:
            O[u] = True
            Path[pos] = u
            if hamiltonian(u, n, macierz, O, Path, pos + 1, start):
                return True
            O[u] = False
            Path[pos] = -1

    return False


def hcycle(macierz, n):
    for start in range(n):
        O = [False] * n
        Path = [-1] * (n + 1)
        O[start] = True
        Path[0] = start

        if hamiltonian(start, n, macierz, O, Path, 1, start):
            Path[n] = start
            return [v + 1 for v in Path]
    return None

#Algorytm Fleury'ego (cykl Eulera)
def liczba_spojnych_skladowych(macierz, n):
    odwiedzone = [False] * n
    count = 0
    for v in range(n):
        if not odwiedzone[v]:
            stack = [v]
            odwiedzone[v] = True
            while stack:
                node = stack.pop()
                for u in range(n):
                    if macierz[node][u] == 1 and not odwiedzone[u]:
                        odwiedzone[u] = True
                        stack.append(u)
            count += 1
    return count


def czy_most(macierz, u, v, n):
    macierz[u][v] -= 1
    macierz[v][u] -= 1
    spojnosc_przed = liczba_spojnych_skladowych(macierz, n)
    macierz[u][v] += 1
    macierz[v][u] += 1
    spojnosc_po = liczba_spojnych_skladowych(macierz, n)
    return spojnosc_po > spojnosc_przed

def znajdz_cykl_eulera(macierz, n):
    for i in range(n):
        if sum(macierz[i]) % 2 != 0:
            return None

    kopia_macierzy = [row[:] for row in macierz]

    stos = []
    cykl = []

    start = next((i for i in range(n) if sum(kopia_macierzy[i]) > 0), None)
    if start is None:
        return None
    stos.append(start)
    while stos:
        v = stos[-1]
        for u in range(n):
            if kopia_macierzy[v][u] > 0:
                if not czy_most([row[:] for row in kopia_macierzy], v, u, n) or sum(kopia_macierzy[v]) == 1:
                    kopia_macierzy[v][u] -= 1
                    kopia_macierzy[u][v] -= 1
                    stos.append(u)
                    break
        else:
            cykl.append(stos.pop())
    return [v + 1 for v in cykl[::-1]]

def czy_nastepna(u, v, macierz_grafu, liczba_wierzcholkow):
    def dfs_count(wezel, odwiedzone):
        odwiedzone[wezel] = True
        count = 1
        for i in range(liczba_wierzcholkow):
            if macierz_grafu[wezel][i] != 0 and not odwiedzone[i]:
                count += dfs_count(i, odwiedzone)
        return count

    count = 0
    for i in range(liczba_wierzcholkow):
        if macierz_grafu[u][i] != 0:
            count += 1
    if count == 1:
        return True

    visited_before = [False] * liczba_wierzcholkow
    count_before = dfs_count(u, visited_before)

    original = macierz_grafu[u][v]
    macierz_grafu[u][v] = 0

    visited_after = [False] * liczba_wierzcholkow
    count_after = dfs_count(u, visited_after)

    macierz_grafu[u][v] = original

    return count_before == count_after
#Algorytmy z macierza grafu
def euler_cycle_macierz_grafu(wierzcholek_startowy, macierz_grafu, liczba_wierzcholkow):
    path = []
    visited_v = [[] for _ in range(liczba_wierzcholkow)]
    def dfs_aeg(u):
        for v in range(liczba_wierzcholkow):
            if v not in visited_v[u] and 2 * liczba_wierzcholkow + 1 <= macierz_grafu[u][v] <= 3 * liczba_wierzcholkow:
                visited_v[u].append(v)
                macierz_grafu[u][v] = 0
                dfs_aeg(v)
        for v in range(liczba_wierzcholkow):
            if v not in visited_v[u] and 1 <= macierz_grafu[u][v] <= liczba_wierzcholkow and czy_nastepna(u, v, macierz_grafu, liczba_wierzcholkow):
                visited_v[u].append(v)
                macierz_grafu[u][v] = 0
                dfs_aeg(v)
        path.append(u+1)
    dfs_aeg(wierzcholek_startowy)
    if path[-1] != path[0]:
        return "Nie ma cyklu eulera"
    else:
        return path[::-1]


def hamiltonian_cycle_macierz_grafu(wierzcholek_startowy, macierz_grafu, liczba_wierzcholkow):
    path = []
    visited = [False] * liczba_wierzcholkow

    def dfs_hamilton(u, count):
        visited[u] = True
        path.append(u + 1)

        if count == liczba_wierzcholkow and macierz_grafu[u][wierzcholek_startowy] != 0:
            path.append(wierzcholek_startowy + 1)
            return True

        for v in range(liczba_wierzcholkow):
            if (1 <= macierz_grafu[u][v] <= liczba_wierzcholkow or 2 * liczba_wierzcholkow + 1 <= macierz_grafu[u][v] <= 3 * liczba_wierzcholkow) and not visited[v]:
                if dfs_hamilton(v, count + 1):
                    return True
        visited[u] = False
        path.pop()
        return False

    if dfs_hamilton(wierzcholek_startowy, 1):
        return path
    else:
        return "Nie ma cyklu Hamiltona"
#---------------------------

def main_menu():
    print("\n=== MENU GŁÓWNE ===")
    print("1. Wprowadź dane z pliku")
    print("2. Wprowadź dane z klawiatury")
    print("0. Wyjście")
    choice = input("Wybierz opcję: ")
    return choice


def algorithm_menu():
    print("\n=== WYBIERZ ALGORYTM ===")
    print("1. Znajdź cykl Hamiltona (macierz grafu)")
    print("2. Znajdź cykl Hamiltona (macierz sąsiedztwa)")
    print("3. Znajdź cykl Eulera (macierz grafu)")
    print("4. Znajdź cykl Eulera (macierz sąsiedztwa)")
    print("0. Powrót")
    choice = input("Wybierz opcję: ")
    return choice


def input_from_keyboard():
    print("\nWprowadź dane grafu:")
    n = int(input("Podaj liczbę wierzchołków: "))
    m = int(input("Podaj liczbę krawędzi: "))
    print("Podaj krawędzie w formacie 'u v' (oddzielone spacją):")

    krawedzie = []
    for _ in range(m):
        u, v = map(int, input().split())
        krawedzie.append([u, v])

    with open("temp_graph.txt", 'w') as f:
        f.write(f"{n} {m}\n")
        for u, v in krawedzie:
            f.write(f"{u} {v}\n")

    return "temp_graph.txt"


def process_hamiltonian_cycle_macierz_grafu(filename):
    krawedzie = wczytaj_krawedzie_z_pliku(filename)
    with open(filename, 'r') as plik:
        pierwsza_linia = plik.readline().split()
        liczba_wierzcholkow = int(pierwsza_linia[0])

    final_macierz_grafu = macierz_grafu(liczba_wierzcholkow, filename, krawedzie)
    final_macierz_grafu = [row[1:] for row in final_macierz_grafu[:-1]]

    print("\nMacierz grafu:")
    for row in final_macierz_grafu:
        print(row)

    result = hamiltonian_cycle_macierz_grafu(0, final_macierz_grafu, liczba_wierzcholkow)
    print("\nWynik:", result)


def process_hamiltonian_cycle_adj(filename):
    macierz = wczytaj_z_pliku(filename)
    n = len(macierz)
    cykl = hcycle(macierz, n)
    print("\nMacierz sąsiedztwa:")
    for row in macierz:
        print(row)
    print("\nWynik:", "Cykl Hamiltona:" if cykl else "Brak cyklu Hamiltona:", cykl)


def process_euler_cycle_mg(filename):
    krawedzie = wczytaj_krawedzie_z_pliku(filename)
    with open(filename, 'r') as plik:
        pierwsza_linia = plik.readline().split()
        liczba_wierzcholkow = int(pierwsza_linia[0])

    final_macierz_grafu = macierz_grafu(liczba_wierzcholkow, filename, krawedzie)
    final_macierz_grafu = [row[1:] for row in final_macierz_grafu[:-1]]

    print("\nMacierz grafu:")
    for row in final_macierz_grafu:
        print(row)

    result = euler_cycle_macierz_grafu(0, final_macierz_grafu, liczba_wierzcholkow)
    print("\nWynik:", result)


def process_euler_cycle_adj(filename):
    macierz = wczytaj_z_pliku(filename)
    n = len(macierz)
    cykl = znajdz_cykl_eulera(macierz, n)
    print("\nMacierz sąsiedztwa:")
    for row in macierz:
        print(row)
    print("\nWynik:", "Cykl Eulera:" if cykl else "Brak cyklu Eulera:", cykl)


def main():
    while True:
        choice = main_menu()

        if choice == '0':
            print("Zamykanie programu...")
            break

        elif choice == '1':
            filename = input("Podaj nazwę pliku: ")
            try:
                with open(filename, 'r'):
                    pass
            except FileNotFoundError:
                print("Plik nie istnieje!")
                continue

        elif choice == '2':
            filename = input_from_keyboard()

        else:
            print("Nieprawidłowy wybór!")
            continue

        while True:
            algo_choice = algorithm_menu()

            if algo_choice == '0':
                break

            elif algo_choice == '1':
                process_hamiltonian_cycle_macierz_grafu(filename)

            elif algo_choice == '2':
                process_hamiltonian_cycle_adj(filename)

            elif algo_choice == '3':
                process_euler_cycle_mg(filename)

            elif algo_choice == '4':
                process_euler_cycle_adj(filename)

            else:
                print("Nieprawidłowy wybór!")

        if choice == '2':
            import os
            os.remove(filename)


if __name__ == "__main__":
    main()
