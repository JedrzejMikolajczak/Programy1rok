wymiary = list(map(int, input().split()))
kolumny = wymiary[0]
wiersze = wymiary[1]
t = []
final_t=[]
for j in range(wiersze):
    final_t.append([0]*kolumny)

kolumna = 0
for i in range(wiersze):
    t.append(list(map(int, input().split())))
for i in range(kolumny):
    tmp = []
    for j in range(wiersze):
        tmp.append(t[j][i])
    tmp.sort()
    for z in range(len(tmp)):
        final_t[z][kolumna] = tmp[z]
    kolumna+=1
for line in final_t:
    print(" ".join(map(str,line)))


