x = int(input())
t = list(map(int,input().split()))
def sumco2(t):
    s = 0
    for i in range(0,len(t),2):
        s+=t[i]
    return s
def sumco3(t):
    s = 0
    for i in range(0,len(t),3):
        s+=t[i]
    return s
max_sum = 0
finalA = []
finalB = []
for a in range(x+1):
    for b in range(x+1):
        A = t[a:b]
        if A != []:
            for i in range(x + 1):
                for j in range(x + 1):
                    B = t[i:j]
                    if sumco2(A) == sumco3(B) and sumco2(A) > max_sum:
                        max_sum = sumco2(A)
                        finalA = A
                        finalB = B
print(max_sum)

