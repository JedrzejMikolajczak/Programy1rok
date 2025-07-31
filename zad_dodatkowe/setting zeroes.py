import copy
wym = list(map(int,input().split()))
wiersze = wym[0]
kolumny = wym[1]
t = []
for i in range(wiersze):
    t.append(list(map(int, input().split())))
new_t = copy.deepcopy(t)
for i in range(wiersze):
    for j in range(kolumny):
        if t[i][j] == 0:
            for a in range(kolumny):
                new_t[i][a] = 0
            for z in range(wiersze):
                new_t[z][j] = 0
for line in new_t:
        print(" ".join(map(str, line)))