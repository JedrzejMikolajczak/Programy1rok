d = int(input())
final_map = []
for i in range(d):
    a = input()
    final_map.append(list(map(int, a)))
def czySasiad(map, x, y):
    if x < 0 or x >= d or y < 0 or y >= d or map[x][y] == 0:
        return
    map[x][y] = 0
    czySasiad(map, x + 1, y)
    czySasiad(map, x - 1, y)
    czySasiad(map, x, y + 1)
    czySasiad(map, x, y - 1)
l_sasiadow = 0
for i in range(d):
    for j in range(d):
        if final_map[i][j] == 1:
            l_sasiadow += 1
            czySasiad(final_map, i, j)

print(l_sasiadow)
