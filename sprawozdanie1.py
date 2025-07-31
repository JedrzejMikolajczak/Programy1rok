import time
import random
import sys
sys.setrecursionlimit(2000000)  # Zwiększenie limitu rekursji

start_time = time.time()
licznik=0
def merge_sort(tab):
    if len(tab) <= 1:
        return tab
    srodek = len(tab) // 2
    lewo = merge_sort(tab[:srodek])
    prawo = merge_sort(tab[srodek:])
    return merge(lewo, prawo)
def merge(l, r):
    global licznik
    licznik+=1
    merged = []
    i=0
    j=0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    while i < len(l):
        merged.append(l[i])
        i += 1
    while j < len(r):
        merged.append(r[j])
        j += 1
    return merged
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
def heapsort_malejaco(arr):
    n = len(arr)
    buduj_kopiec_min(arr)
    for i in range(n - 1):
        arr[0], arr[n - 1 - i] = arr[n - 1 - i], arr[0]
        j = 0
        rozmiar_kopca = n - 1 - i
        while 2 * j + 1 < rozmiar_kopca:
            left = 2 * j + 1
            right = 2 * j + 2
            smallest = j
            if left < rozmiar_kopca and arr[left] < arr[smallest]:
                smallest = left
            if right < rozmiar_kopca and arr[right] < arr[smallest]:
                smallest = right
            if smallest == j:
                break
            arr[j], arr[smallest] = arr[smallest], arr[j]
            j = smallest
    return arr
def shell_sort(t):
    n = len(t)
    przyrost_hibbarda = []
    i = 1
    while (2 ** i - 1) < n:
        przyrost_hibbarda.append(2 ** i - 1)
        i += 1
    przyrost_hibbarda.reverse()

    for przyrost in przyrost_hibbarda:
        print(przyrost)
        for j in range(przyrost, n):
            key = t[j]
            i = j
            while i >= przyrost and t[i - przyrost] > key:
                t[i] = t[i - przyrost]
                i -= przyrost
            t[i] = key

    return t
def generuj_ciag_malejacy(n, min_val=0, max_val=100):
    return sorted([random.randint(min_val, max_val) for _ in range(n)], reverse=True)
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

def quick_sort_rekurencyjnie(t, l, r):
    if l < r:
        q = partition(t, l, r)
        quick_sort_rekurencyjnie(t, l, q-1)
        quick_sort_rekurencyjnie(t, q + 1, r)
    return t

def partition(t, left, right):
    pivot = t[right]  # Pivot to ostatni element
    i = left - 1  # Wskaźnik dla większych elementów

    for j in range(left, right):  # Przeszukujemy od lewej do prawej (bez pivota)
        if t[j] >= pivot:  # Sortowanie malejące
            i += 1
            t[i], t[j] = t[j], t[i]  # Zamiana miejscami

    t[i + 1], t[right] = t[right], t[i + 1]  # Umieszczenie pivota w odpowiednim miejscu
    return i + 1  # Zwracamy indeks pivota


def generuj_tablice(ile_liczb, zakres_dol, zakres_gora):
    t = [random.randint(zakres_dol,zakres_gora) for _ in range(ile_liczb)]
    return t
def wczytaj_z_klawiatury():
    t = []
    n = int(input())
    for i in range(n):
        a = int(input())
        t.append(a)
    return t

def generuj_ciag_v_ksztaltny(n, min_val=0, max_val=100):
    if n < 2:
        return [random.randint(min_val, max_val) for _ in range(n)]
    polowa = n // 2
    lewa_strona = sorted([random.randint(min_val, max_val) for _ in range(polowa)], reverse=True)
    prawa_strona = sorted([random.randint(min_val, max_val) for _ in range(n - polowa)], reverse=False)
    return lewa_strona + [min_val] + prawa_strona
def generuj_ciag_a_ksztaltny(n, min_val=0, max_val=100):
    if n < 2:
        return [random.randint(min_val, max_val) for _ in range(n)]
    polowa = n // 2
    lewa_strona = sorted([random.randint(min_val, max_val) for _ in range(polowa)], reverse=False)
    prawa_strona = sorted([random.randint(min_val, max_val) for _ in range(n - polowa)], reverse=True)
    return lewa_strona + [max_val] + prawa_strona
def generuj_rosnacy_ciag(n, zakres_dol, zakres_gora):
    if n > (zakres_gora - zakres_dol + 1):
        raise ValueError("Nie można wygenerować tylu unikalnych rosnących liczb w podanym zakresie!")

    liczby = sorted(random.sample(range(zakres_dol, zakres_gora + 1), n))
    return liczby
def sredni_czas_sortowania_rekurencyjnego(rozmiar_ciagu, liczba_testow):
    czasy = []
    for _ in range(liczba_testow):
        ciag = generuj_rosnacy_ciag(rozmiar_ciagu,1,rozmiar_ciagu*10)
        start = time.time()
        quick_sort_rekurencyjnie(ciag, 0, len(ciag) - 1)
        end = time.time()
        czasy.append(end - start)
    return round(sum(czasy) / len(czasy),6)

# Przykładowe użycie

#print(sredni_czas_sortowania_rekurencyjnego(10000,10))
t = generuj_tablice(10,1,100)
#print(t)
print(quick_sort_iteracyjnie(t))

end_time = time.time()
final_time = end_time-start_time
print(f"Czas: {final_time:.6f} s")