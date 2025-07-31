wymiar = int(input())
t = []
for i in range(wymiar):
    t.append(list(map(int,input().split())))
tablica_jedynek = []
for i in range(wymiar):
    for j in range(wymiar):
        if t[i][j] == 1:
            tablica_jedynek.append([i+1,j+1])
current = []
t_distance = []
t_distance.append(1000)
for i in range(len(tablica_jedynek)):
    current = tablica_jedynek[i]
    for j in range(len(tablica_jedynek)):
        current2 = tablica_jedynek[j]
        if current != current2:
            if  current2[0]%current[0]==0 and current2[1]%current[1]==0:
                distance = abs(current[0]-current2[0])+abs(current[1]-current2[1])
                t_distance.append(distance)
            else:
                t_distance.append(1000)
print(min(t_distance))

