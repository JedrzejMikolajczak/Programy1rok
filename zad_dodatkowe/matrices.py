import copy
wymiar = int(input())
t1 = []
for i in range(wymiar):
    t1.append(input().split())
t2 = []
for i in range(wymiar-1):
    t2.append(list(map(str, input().split())))
newt1 = []
for i in range(wymiar-1):
    newt1.append([0]*(wymiar-1))
tmp = 0
def usun_wiersz_i_kolumne(t,wymiar,jaki_wiersz, jaka_kolumna):
    newt1 = []
    for i in range(wymiar):
        if i != jaki_wiersz:
            newt1.append(t[i])
        else:continue
    for i in range(wymiar-1):
        if jaka_kolumna==i:
            for j in range(wymiar-1):
                del newt1[j][i]
        else:
            continue
    return newt1


for i in range(wymiar):
    for j in range(wymiar):
        test = copy.deepcopy(t1)
        if usun_wiersz_i_kolumne(test,wymiar,i,j)==t2:
            print("True")
            exit()
print("False")
