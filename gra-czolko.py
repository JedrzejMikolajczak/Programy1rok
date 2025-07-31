class Gracz:
    def __init__(self, nazwa, zgadywana_postac):
        self.nazwa = nazwa
        self.zgadywana_postac = zgadywana_postac
    def __str__(self):
        return f"{self.nazwa},{self.zgadywana_postac}"
players = []
start = True
while start:
    print("1. Dodaj gracza (Imie, wymyslona przez niego postac")
    print("2. Zakoncz dodawanie graczy")
    answer = input()
    answer = int(answer)
    if answer == 1:
        print("Podaj imie gracza: ")
        name = input()
        print("Podaj wymyśloną przez ciebie postać: ")
        postac = input()
        connect = name + ";" + postac
        players.append(connect)
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if answer == 2:
        start = False
lista = []
for i in range(len(players)):
    lista.append(players[i].rstrip().split(";"))

gracze = []
for i in range(len(lista)):
    gracze.append(lista[i][0])
postacie = []
for i in range(len(lista)):
    postacie.append(lista[i][1])

final_profiles = []
#tworzenie profili graczy

for i in range(len(lista)):
    nr_postaci = 0
    if len(lista)-1 == i:
        nr_postaci = 0
    else:
        nr_postaci = i+1
    player_profile = Gracz(gracze[i],postacie[nr_postaci])
    final_profiles.append(player_profile.__str__())
#wypisywanie list dla graczy
tmp = 0
for i in range(len(players)):
    tmp = i
    tmp_string = ""
    for j in range(len(final_profiles)):
        if j != tmp:
            tmp_string+=final_profiles[j]
            tmp_string+="\n"
    file = open(f'{gracze[i]}.txt','a')
    file.write(tmp_string)
    file.close()
