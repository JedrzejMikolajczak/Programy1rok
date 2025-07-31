wymiar = int(input())
t = []
for i in range(wymiar):
    t.append(list(map(int,input().split())))
liczba_elementów = wymiar^2
tmp = []
for i in range(wymiar):
    for j in range(wymiar):

