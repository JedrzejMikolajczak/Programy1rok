t = []
for i in range(9):
    t.append(list(map(int, input().split())))
for i in range(9):
    tmp = []
    for j in range(9):
        if t[i][j] in tmp or t[i][j] <1 or t[i][j]>9:
            print("False")
            exit()
        else:
            tmp.append(t[i][j])
for i in range(9):
    tmp = []
    for j in range(9):
        if t[j][i] in tmp or t[i][j] <1 or t[i][j]>9:
            print("False")
            exit()
        else:
            tmp.append(t[j][i])
tmp = []
conuter = 0
for i in range(9):
    if t[i][i] <1 or t[i][i]>9:
        print("True")
        exit()
    elif t[i][i] in tmp:
        print("True")
        exit()
    else:
        tmp.append(t[i][i])
        conuter+=1
tmp = []
for i in range(8,-1,-1):
    if t[i][8-i] <1 or t[i][8-i]>9:
        print("True")
        exit()
    elif t[i][8-i] in tmp:
        print("True")
        exit()
    else:
        tmp.append(t[i][8-i])
        conuter += 1
if conuter==18:
    print("X")
else:
    print("True")