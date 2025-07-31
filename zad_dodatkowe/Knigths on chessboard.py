a = int(input())
chessboard = []
for i in range(a):
    chessboard.append(input())
print(chessboard)
def czy_mozna_sie_ruszyc(x,y):
    if x>=0 and x<=a-1 and y>=0 and y<=a-1:
        return True
    return False
def possible_moves(figura,pozycja_wiersz, pozycja_kolumna, szachownica):
    to_return = 0
    if figura == "o":
        return 0
    moves = [[-2,-1],[-2,1],[-1,-2],[1,2],[-1,2],[1,-2],[2,1],[2,-1]]
    for i in range(len(moves)):
        new_x = pozycja_wiersz+moves[i][0]
        new_y = pozycja_kolumna+moves[i][1]
        if czy_mozna_sie_ruszyc(new_x,new_y):
            if szachownica[new_x][new_y] == "s":
                to_return+=1
    return to_return
suma = 0
for i in range(a):
    for j in range(a):
        suma+=possible_moves(chessboard[i][j], i, j, chessboard)
print(suma)