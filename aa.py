move = int(input())
s = input()
final_s = ""
for el in s:
    if s.isupper():
        a = ""
        a+=chr((ord(a)-move-65) % 26 + 65)
    else:
        a = ""
        a +=chr((ord(s)-move-65) % 26 + 65)
print(final_s)