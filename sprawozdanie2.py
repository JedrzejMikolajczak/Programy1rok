import random
import time
class drzewo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def zbuduj_drzewo_z_kopca(arr):
    if not arr:
        return None
    nodes = [drzewo(value) for value in arr]
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr):
            nodes[i].left = nodes[left]
        if right < len(arr):
            nodes[i].right = nodes[right]
    return nodes[0]
def buduj_kopiec_min(arr):
    n = len(arr)
    i = n // 2 - 1
    while i >= 0:
        j = i
        while 2 * j + 1 < n:
            left = 2 * j + 1
            right = 2 * j + 2
            smallest = j
            if left < n and arr[left] < arr[smallest]:
                smallest = left
            if right < n and arr[right] < arr[smallest]:
                smallest = right
            if smallest == j:
                break
            arr[j], arr[smallest] = arr[smallest], arr[j]
            j = smallest
        i -= 1
def quick_sort_iteracyjnie(t):
    stack = [(0, len(t) - 1)]
    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = t[right]
            i = left - 1
            for j in range(left, right):
                if t[j] < pivot:
                    i += 1
                    t[i], t[j] = t[j], t[i]
            t[i + 1], t[right] = t[right], t[i + 1]
            pivot_index = i + 1
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))
    return t
def znajdz_mediane(t):
    return t[(len(t) - 1) // 2]
def generowanie_drzewa_AVL(t):
    if not t:
        return None
    t = quick_sort_iteracyjnie(t)
    srodek = (len(t) - 1) // 2
    mediana = t[srodek]
    wezel = drzewo(mediana)
    wezel.left = generowanie_drzewa_AVL(t[:srodek])
    wezel.right = generowanie_drzewa_AVL(t[srodek + 1:])
    return wezel
def pre_order(wezel):
    if wezel:
        print(wezel.value, end=' ')
        pre_order(wezel.left)
        pre_order(wezel.right)
def in_order(wezel):
    if wezel:
        in_order(wezel.right)
        print(wezel.value, end=" ")
        in_order(wezel.left)
def FCFS_BST(t):
    if not t:
        return None
    root = drzewo(t[0])
    for value in t[1:]:
        wstawianie_drzewo_BST(root, value)
    return root
def wstawianie_drzewo_BST(wezel, wartosc):
    if wezel is None:
        return drzewo(wartosc)
    if wartosc < wezel.value:
        wezel.left = wstawianie_drzewo_BST(wezel.left, wartosc)
    else:
        wezel.right = wstawianie_drzewo_BST(wezel.right, wartosc)

    return wezel
def znajdz_maksymalny(wezel):
    start_time = time.perf_counter()
    sciezka = []
    while wezel.right:
        sciezka.append(wezel.value)
        wezel = wezel.right
    sciezka.append(wezel.value)
    end_time = time.perf_counter()
    print(f"Czas znajdowania maksymalnego: {(end_time - start_time) * 1000:.6f} ms")
    return wezel.value, sciezka
def znajdz_minimalny(wezel):
    start_time = time.perf_counter()
    sciezka = []
    while wezel.left:
        sciezka.append(wezel.value)
        wezel = wezel.left
    sciezka.append(wezel.value)
    end_time = time.perf_counter()
    print(f"Czas znajdowania minimalnego: {(end_time - start_time) * 1000:.6f} ms")
    return wezel.value, sciezka
def ktory_poziom(wezel, wartosc, poziom=0):
    if wezel is None:
        return -1
    if wezel.value == wartosc:
        return poziom
    lewy_poziom = ktory_poziom(wezel.left,wartosc,poziom+1)
    if lewy_poziom != -1:
        return lewy_poziom
    return ktory_poziom(wezel.right,wartosc, poziom+1)
def wypisz_wszystkie_na_poziomie(wezel, poziom):
    if wezel is None:
        return
    if poziom == 0:
        print(wezel.value, end=" ")
    else:
        if wezel.left:
            wypisz_wszystkie_na_poziomie(wezel.left, poziom - 1)
        if wezel.right:
            wypisz_wszystkie_na_poziomie(wezel.right, poziom - 1)
def find_min_hmin(wezel):
    path = [wezel.value]
    print(f"Ścieżka do minimalnej wartości: {path}")
    return wezel.value
def find_max_hmin(wezel):
    path = []
    current = wezel
    while current:
        path.append(current.value)
        if current.right:
            current = current.right
        else:
            break
    print(f"Ścieżka do maksymalnej wartości: {path}")
    return current.value
def znajdz_wezel(wezel):
    klucz = int(input("Podaj klucz: "))

    def szukaj(wezel, klucz):
        if wezel is None:
            return None
        if wezel.value == klucz:
            return wezel
        lewy = szukaj(wezel.left, klucz)
        if lewy:
            return lewy
        return szukaj(wezel.right, klucz)

    poddrzewo = szukaj(wezel, klucz)

    if poddrzewo:
        pre_order(poddrzewo)

        wys = wysokosc(poddrzewo)
        print(" ")
        print("wysokość:", wys)
        usun_drzewo_post_order(poddrzewo)
        return poddrzewo
    else:
        return None
def wysokosc(wezel):
    if wezel is None:
        return -1
    lewa_wysokosc = wysokosc(wezel.left)
    prawa_wysokosc = wysokosc(wezel.right)
    return max(lewa_wysokosc, prawa_wysokosc) + 1
def usun_drzewo_post_order(wezel):
    if wezel is None:
        return
    usun_drzewo_post_order(wezel.left)
    usun_drzewo_post_order(wezel.right)
    wezel.left = None
    wezel.right = None
def generuj_tablice(ile_liczb, zakres_dol, zakres_gora):
    return [random.randint(zakres_dol,zakres_gora) for _ in range(ile_liczb)]
while True:
        print("\nWybierz typ drzewa:")
        print("1. Drzewo BST")
        print("2. Drzewo AVL")
        print("3. Drzewo HMIN")
        print("4. Wyjście")

        choice = input("Twój wybór: ")
        if choice == "4":
            print("Zakończono program.")
            exit()

        tree_type = None
        if choice == "1":
            tree_type = "BST"
        elif choice == "2":
            tree_type = "AVL"
        elif choice == "3":
            tree_type = "HMIN"
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            continue

        print("\nWybierz źródło danych:")
        print("1. Z pliku")
        print("2. Generator losowy")
        data_choice = input("Twój wybór: ")
        tab = []
        if data_choice == "1":
            with open("plik.txt", "r") as plik:
                tab = list(map(int, plik.readline().split()))
                print(znajdz_mediane(tab))
            print(tab)

        elif data_choice == "2":
            size = int(input("Podaj liczbę elementów do wygenerowania: "))
            tab = generuj_tablice(size,1,size*100)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            continue

        while True:
            print("\nWybierz operację:")
            print("1. Znajdź min i max")
            print("2. Znajdź poziom węzła o podanym kluczu")
            print("3. Wypisz elementy na tym samym poziomie")
            print("4. Wypisz elementy drzewa w porządku malejącym")
            print("5. Pre-order poddrzewa, wysokość i usunięcie")
            print("6. Powrót do wyboru drzewa")

            op_choice = input("Twój wybór: ")
            if choice == "1":
                wezel = FCFS_BST(tab)
            elif choice == "2":
                wezel = generowanie_drzewa_AVL(tab)
                tree_type = "AVL"
            elif choice == "3":
                tree_type = "HMIN"
                buduj_kopiec_min(tab)
                wezel = zbuduj_drzewo_z_kopca(tab)
            if op_choice == "1":
                if choice == "3":
                    start_time = time.perf_counter()
                    min_value = find_min_hmin(wezel)
                    print(f"Minimalna wartość: {min_value}")
                    max_value = find_max_hmin(wezel)
                    print(f"Maksymalna wartość: {max_value}")
                    end_time = time.perf_counter()
                    print("\n")
                    print(f"Czas: {(end_time - start_time) * 1000:.6f} ms")
                else:
                    print(znajdz_minimalny(wezel))
                    print(znajdz_maksymalny(wezel))
            elif op_choice == "2":
                key = int(input("Podaj klucz: "))
                print(ktory_poziom(wezel,key,poziom=0))
            elif op_choice == "3":
                key = int(input("Podaj klucz: "))
                wypisz_wszystkie_na_poziomie(wezel, ktory_poziom(wezel, key, poziom=0))
            elif op_choice == "4":
                start_time = time.perf_counter()
                in_order(wezel)
                end_time = time.perf_counter()
                print("\n")
                print(f"Czas: {(end_time - start_time) * 1000:.6f} ms")
            elif op_choice == "5":
                poddrzewo = znajdz_wezel(wezel)
            elif op_choice == "6":
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
