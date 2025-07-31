def wczytaj_dane():
    wybor = input("Wybierz sposób wczytania danych (1 - klawiatura, 2 - plik): ")
    if wybor == "1":
        try:
            n, c = map(int, input("Podaj liczbę przedmiotów i pojemność plecaka: ").split())
            przedmioty = []
            for i in range(n):
                w, p = map(int, input(f"Podaj masę i wartość przedmiotu nr {i+1}: ").split())
                przedmioty.append((w, p, i+1))
            return przedmioty, c
        except Exception as e:
            print("Błąd danych:", e)
            return None, None
    elif wybor == "2":
        nazwa = input("Podaj nazwę pliku: ")
        try:
            with open(nazwa, "r") as f:
                lines = f.readlines()
                n, c = map(int, lines[0].split())
                przedmioty = []
                for i, line in enumerate(lines[1:n+1]):
                    w, p = map(int, line.split())
                    przedmioty.append((w, p, i+1))
                return przedmioty, c
        except Exception as e:
            print("Błąd pliku:", e)
            return None, None
    else:
        print("Niepoprawny wybór.")
        return None, None

def algorytm_silowy(przedmioty, c):
    n = len(przedmioty)
    max_wartosc = 0
    najlepszy_zbior = []
    # przeglad wszystkich mozliwych podzbiorow, kazdy z nich reprezentowany jest przez liczbe binarna o n bitach
    for i in range(1, 2**n):
        wybor = []
        for j in range(n):
            if (i >> j) & 1:
                # sprawdzenie czy jty bit w liczbie i jest rowny 1
                # gdy tak to dodajemy j-ty przedmiot do wybor
                wybor.append(przedmioty[j])
        masa = sum(w for w, p, idx in wybor)
        wartosc = sum(p for w, p, idx in wybor)
        if masa <= c and wartosc > max_wartosc:
            max_wartosc = wartosc
            najlepszy_zbior = wybor
    return najlepszy_zbior, max_wartosc

def zwroc_wartosc_na_jednostke(t):
    return t[0]

def algorytm_zachlanny(przedmioty, c):
    przedmioty.sort(key=zwroc_wartosc_na_jednostke, reverse=True)
    masa = 0
    wartosc = 0
    rozwiazanie = []
    for w, p, idx in przedmioty:
        if masa + w <= c:
            masa += w
            wartosc += p
            rozwiazanie.append((w, p, idx))

    opt_rozw, opt_wartosc = algorytm_silowy(przedmioty, c)
    czy_optymalne = wartosc == opt_wartosc
    return rozwiazanie, wartosc, masa, czy_optymalne

def algorytm_dynamiczny(przedmioty, c):
    n = len(przedmioty)
    # Inicjalizacja macierzy V (n+1) x (c+1)
    V = [[0] * (c + 1) for _ in range(n + 1)]

    # wypelnianie funckja rekurencyjna Bellmana
    for i in range(1, n + 1):
        w_i, p_i, _ = przedmioty[i - 1]
        for j in range(c + 1):
            if w_i > j:
                V[i][j] = V[i - 1][j] # nie bierzemy
            else:
                V[i][j] = max(V[i - 1][j], V[i - 1][j - w_i] + p_i)

    wynik = []
    j = c
    for i in range(n, 0, -1):
        if V[i][j] != V[i - 1][j]:  # gdy sa rozne to ity zostal wybrany
            wynik.append(przedmioty[i - 1])
            j -= przedmioty[i - 1][0]  # - waga tego przedmiotu

    wynik.reverse()
    return wynik, V[n][c]


def wyswietl_rozwiazanie(nazwa, rozwiazanie, wartosc):
    masa = sum(w for w, p, idx in rozwiazanie)
    print(f"\nAlgorytm: {nazwa}")
    print(f"Wybrane przedmioty: {[idx for w, p, idx in rozwiazanie]}")
    print(f"Sumaryczna masa: {masa}")
    print(f"Wartość funkcji celu: {wartosc}")

def main():
    przedmioty, c = wczytaj_dane()
    if not przedmioty:
        return

    # Algorytm siłowy
    rozw_ab, wart_ab = algorytm_silowy(przedmioty, c)
    wyswietl_rozwiazanie("Siłowy: ", rozw_ab, wart_ab)

    # Algorytm zachłanny
    rozw_az, wart_az, masa_az, opt = algorytm_zachlanny(przedmioty.copy(), c)
    wyswietl_rozwiazanie("Zachłanny: ", rozw_az, wart_az)
    print("Czy rozwiązanie optymalne?", "TAK" if opt else "NIE")

    # Algorytm programowania dynamicznego
    rozw_ad, wart_ad = algorytm_dynamiczny(przedmioty, c)
    wyswietl_rozwiazanie("Dynamiczny: ", rozw_ad, wart_ad)

if __name__ == "__main__":
    main()