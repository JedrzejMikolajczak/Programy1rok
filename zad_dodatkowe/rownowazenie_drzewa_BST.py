import math
import random
import time
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
def generuj_tablice(ile_liczb, zakres_dol, zakres_gora):
    return [random.randint(zakres_dol, zakres_gora) for _ in range(ile_liczb)]
class drzewo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def rotacja_prawo(wezel):
    if not wezel or not wezel.left:
        return wezel
    child = wezel.left
    wezel.left = child.right
    child.right = wezel
    return child


def rotacja_lewo(wezel):
    if not wezel or not wezel.right:
        return wezel
    child = wezel.right
    wezel.right = child.left
    child.left = wezel
    return child
def generuj_winorosl(wezel):
    winorosl = drzewo(None)
    winorosl.right = wezel
    wezel = winorosl
    while wezel.right:
        if wezel.right.left:
            wezel.right = rotacja_prawo(wezel.right)
        wezel = wezel.right
    return winorosl.right
def liczba_elementow(root):
    n, current = 0, root
    while current:
        n += 1
        current = current.right
    return n
def rotacje_lewo(root, count):
    pseudo_root = drzewo(None)
    pseudo_root.right = root
    parent = pseudo_root
    for _ in range(count):
        if parent.right:
            parent.right = rotacja_lewo(parent.right)
            parent = parent.right
    return pseudo_root.right
def balansuj_drzewo(root):
    root = generuj_winorosl(root)
    n = liczba_elementow(root)
    # Krok 1
    w = math.floor(math.log2(n + 1))
    x = n + 1 - (1 << w)
    root = rotacje_lewo(root, x)
    # Krok 2
    y = n - x
    while y > 1:
        root = rotacje_lewo(root, y // 2)
        y //= 2
    return root
def pre_order(wezel):
    if wezel:
        print(wezel.value, end=' ')
        pre_order(wezel.left)
        pre_order(wezel.right)
start_time = time.perf_counter()
#t = [10,15,12,6,3,8,16,5,4]
#root = FCFS_BST(t)
root = drzewo(1)
root.right = drzewo(2)
root.right.right = drzewo(3)
root.right.right.right = drzewo(4)
root.right.right.right.right = drzewo(5)
root.right.right.right.right.right = drzewo(6)
root.right.right.right.right.right.right = drzewo(7)
print("Drzewo przed balansowaniem:")
pre_order(root)
print("\n")

root = balansuj_drzewo(root)

print("Drzewo po balansowaniu:")
pre_order(root)
print("\n")
end_time = time.perf_counter()
print(f"Czas znajdowania maksymalnego: {(end_time - start_time) * 1000:.6f} ms")