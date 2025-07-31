ile = int(input())
t = []
for i in range(ile):
    t.append(list(map(int, input().split())))
p = []
for i in range(len(t)):
    px1 = t[i]
    for j in range(len(t)):
        px2 = t[j]
        if px1 != px2:
            for k in range(j+1, len(t)):
                px3 = t[k]
                if px3 != px2 and px3!=px1:
                    x1 = px2[0] - px1[0]
                    y1 = px2[1] - px1[1]
                    x2 = px3[0] - px1[0]
                    y2 = px3[1] - px1[1]
                    pole = abs(x1*y2-y1*x2)/2
                    if pole > 0:
                        p.append(pole)
print(f"{min(p)} {max(p)}")