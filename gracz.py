class Gracz:
    def __init__(self, nazwa, zgadywana_postac):
        self.nazwa = nazwa
        self.zgadywana_postac = zgadywana_postac
    def __str__(self):
        return f"{self.nazwa},{self.zgadywana_postac}"
with open('lista_graczy.txt','r')as plik:
    lista = plik.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i].rstrip().split(",")
print(len(lista))
gracze = []
for i in range(len(lista)):
    gracze.append(lista[i][0])
postacie = []
for i in range(len(lista)):
    postacie.append(lista[i][2])

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
print(final_profiles[1])




