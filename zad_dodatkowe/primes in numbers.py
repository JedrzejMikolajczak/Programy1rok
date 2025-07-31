a = int(input())
t = list(str(a))
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
res = []
for i in range(len(t)):
    num = ""
    for j in range(i, len(t)):
        num += t[j]
        if isprime(int(num)):
            if int(num) not in res:
                res.append(int(num))
res.sort(key=str, reverse=True)
for i in range(len(res)):
    print(res[i])