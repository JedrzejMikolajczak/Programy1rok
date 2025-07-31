newm = list(map(int,input().split()))
matrix = []
for i in range(newm[0]):
    matrix.append(list(map(int,input().split())))
sorted_matrix = [[0 for _ in range(newm[1])] for _ in range(newm[0])]
linear_matrix = []
for i in range(newm[0]):
    for j in range(newm[1]):
        linear_matrix.append(matrix[i][j])
k = 0
ktory = 0
linear_matrix.sort()
for i in range(newm[0]):
    line = []
    for j in range(newm[1]):
        el = linear_matrix[i+j*newm[0]]
        line.append(el)
    print(" ".join(map(str,line)))

