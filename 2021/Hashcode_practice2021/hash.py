
class Pizza:
    def __init__(self, id, numero_ingredienti, lista_ingredienti):
        self.id = id
        self.numero_ingredienti = numero_ingredienti
        self.lista_ingredienti = lista_ingredienti
    
    def __gt__(self, p):
        return self.numero_ingredienti<p.numero_ingredienti
    
    def unione(self, p):
        return len(set(self.lista_ingredienti) | set(p.lista_ingredienti))
    
class Team:
    def __init__(self, num):
        self.num = num
        self.pizze = []
    def stampa(self):
        print(f'Pizza per team da {self.num}, con pizze {self.pizze}')


def leggiFile(file):
    f = open(file, 'r')
    prima = f.readline()
    global totPizze
    global numTeam2
    global numTeam3
    global numTeam4
    global numPizzeTotali
    totPizze, numTeam2, numTeam3, numTeam4 = list(map(int, prima.strip().split()))
    i=0
    global listaPizze
    for riga in f:
        riga = riga.strip().split()
        indice = int(i)
        numero_ingredienti = int(riga.pop(0))
        listaPizze.append(Pizza(indice, numero_ingredienti, riga))
        i+=1
    listaPizze.sort()
    numPizzeTotali = len(listaPizze)

#######################################################################################################################################

def calcolaFineBlocco():
    global numTeam4
    global numTeam3
    global numTeam2
    global numPizzeTotali
    if numTeam4>0 and numPizzeTotali>=4:
        return min(8,numPizzeTotali)
    elif numTeam3>0 and numPizzeTotali>=3:
        return min(6,numPizzeTotali)
    elif numTeam2>0 and numPizzeTotali>=2:
        return min(4,numPizzeTotali)
    else:
        return 0

def riempiteam4():
    global listaPizze
    global numTeam4
    n_team = numTeam4

    COSTANTE = 12
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
    index = calcolaFineBlocco()
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]

    NUMERO_PIZZE_RICHIESTE = COSTANTE
    indici_scelti = []
    while numTeam4>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE:
        team = Team(4) #########
        listaTeam.append(team)
        if len(listaPizze)<=7:
            tea.pizze = listaPizze[0:4]
            listaPizze = listaPizze[4:]
            break
        indici_scelti = [x for x in range(COSTANTE)]
        for i in range(COSTANTE):      # unione insiemi
            if i not in indici_scelti:
                continue
            for j in range(COSTANTE):
                if j in indici_scelti:
                    matrix[i][j] = pizze_scelte[i].unione(pizze_scelte[j])
        index_max_row = None
        index_max_col = None
        l_max_index = [-1 for i in range(COSTANTE)]
        l_max = [-1 for i in range(COSTANTE)]
        for i in range(COSTANTE):      # scelta primo e secondo
            l_max[i] = max(matrix[i])
            l_max_index[i] = matrix[i].index(max(matrix[i]))
        index_max_row = l_max.index(max(l_max))
        index_max_col = l_max_index[index_max_row]

        team.pizze.append(listaPizze[index_max_col].id)
        team.pizze.append(listaPizze[index_max_row].id)
        matrix[index_max_row][index_max_col] = -1
        mas = -1
        terzo_index = None
        for i in range(COSTANTE):      # scelta terzo
            if i == index_max_row or i == index_max_col:
                continue
            if matrix[index_max_row][i] + matrix[i][index_max_col] > mas:
                mas = matrix[index_max_row][i] + matrix[i][index_max_col]
                terzo_index = i
        
        matrix[index_max_row][terzo_index] = -1
        team.pizze.append(listaPizze[terzo_index].id)
        
        mas = -1
        quarto_index = None
        for i in range(COSTANTE):      # scelta quarto
            if i == index_max_row or i == index_max_col or i == terzo_index:
                continue
            if matrix[i][index_max_row] + matrix[i][index_max_col] + matrix[i][terzo_index] > mas:
                mas  = matrix[i][index_max_row] + matrix[i][index_max_col] + matrix[i][terzo_index]
                quarto_index = i

        team.pizze.append(listaPizze[quarto_index].id)

        
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)
        indici_scelti.append(quarto_index)

        for i in range(len(matrix)):        # mette -1 nelle celle scelte
            if i == index_max_col or i == index_max_row or i == terzo_index or i == quarto_index:
                matrix[i] = [-1 for x in range(COSTANTE)]
            else:
                for j in range(len(matrix[i])):
                    if j == index_max_col or j == index_max_row or j == terzo_index or j == quarto_index:
                        matrix[i][j] = -1

        pizze_scelte[index_max_col] = listaPizze[index]
        pizze_scelte[index_max_row] = listaPizze[index-1]
       # pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[terzo_index] = listaPizze[index-2]
        #pizze_scelte[terzo_index] = listaPizze[index+2]
        pizze_scelte[quarto_index] = listaPizze[index-3]
        #pizze_scelte[quarto_index] = listaPizze[index+3]
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)
        indici_scelti.append(quarto_index)

        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)
        listaPizze.pop(terzo_index)
        listaPizze.pop(quarto_index)

        #index += 4 #####
        index = calcolaFineBlocco()-1

        
        numTeam4-=1
###################################################################################################################
def riempiteam3():
    global listaPizze
    global numTeam3
    n_team = numTeam3
    COSTANTE = 6 ##
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
    index = calcolaFineBlocco()
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]
    print(pizze_scelte)
    NUMERO_PIZZE_RICHIESTE = 6
    indici_scelti = []
    while numTeam3>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE:
        if len(listaPizze)==3:
            team = Team(3)
            team.pizze = listaPizze
            break
        NUMERO_PIZZE_RICHIESTE = 3
        team = Team(3)
        listaTeam.append(team)
        indici_scelti = [x for x in range(COSTANTE)]
        for i in range(COSTANTE):      # unione insiemi
            if i not in indici_scelti:
                continue
            for j in range(COSTANTE):
                if j in indici_scelti:
                    matrix[i][j] = pizze_scelte[i].unione(pizze_scelte[j])
        index_max_row = None
        index_max_col = None
        l_max_index = [-1 for i in range(COSTANTE)]
        l_max = [-1 for i in range(COSTANTE)]
        for i in range(COSTANTE):      # scelta primo e secondo
            l_max[i] = max(matrix[i])
            l_max_index[i] = matrix[i].index(max(matrix[i]))
        index_max_row = l_max.index(max(l_max))
        index_max_col = l_max_index[index_max_row]

        team.pizze.append(listaPizze[index_max_col].id)
        team.pizze.append(listaPizze[index_max_row].id)
        matrix[index_max_row][index_max_col] = -1
        mas = -1
        terzo_index = None
        for i in range(COSTANTE):      # scelta terzo
            if i == index_max_row or i == index_max_col:
                continue
            if matrix[index_max_row][i] + matrix[i][index_max_col] > mas:
                mas = matrix[index_max_row][i] + matrix[i][index_max_col]
                terzo_index = i
        
        matrix[index_max_row][terzo_index] = -1
        team.pizze.append(listaPizze[terzo_index].id)
        

        #for i in range(COSTANTE):
        #    print(matrix[i])
        
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)

        for i in range(len(matrix)):        # mette -1 nelle celle scelte
            if i == index_max_col or i == index_max_row or i == terzo_index:
                matrix[i] = [-1 for x in range(COSTANTE)]
            else:
                for j in range(len(matrix[i])):
                    if j == index_max_col or j == index_max_row or j == terzo_index :
                        matrix[i][j] = -1
        #print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )
        pizze_scelte[index_max_col] = listaPizze[index]
        pizze_scelte[index_max_row] = listaPizze[index-1]
        #pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[terzo_index] = listaPizze[index-2]
        #pizze_scelte[terzo_index] = listaPizze[index+2]
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)
        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)
        listaPizze.pop(terzo_index)

        #index += 3
        index = calcolaFineBlocco()-1
       # print(f'Numero di team: {len(listaTeam)}')
        numTeam3-=1

###########################################################################################################à
def riempiteam2():
    global listaPizze
    global numTeam2
    n_team = numTeam2
    COSTANTE = 4
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
    index = calcolaFineBlocco()-1
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]
    #print(pizze_scelte)
    NUMERO_PIZZE_RICHIESTE = 4
    indici_scelti = []
    while numTeam2>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE and len(listaPizze)>=index:
        if len(listaPizze)==2:
            team = Team(2)
            team.pizze = listaPizze
            listaTeam.append(team)
            break
        NUMERO_PIZZE_RICHIESTE = 2
        team = Team(2)
        listaTeam.append(team)
        indici_scelti = [x for x in range(COSTANTE)]
        for i in range(COSTANTE):      # unione insiemi
            if i not in indici_scelti:
                continue
            for j in range(COSTANTE):
                if j in indici_scelti:
                    matrix[i][j] = pizze_scelte[i].unione(pizze_scelte[j])
        index_max_row = None
        index_max_col = None
        l_max_index = [-1 for i in range(COSTANTE)]
        l_max = [-1 for i in range(COSTANTE)]
        for i in range(COSTANTE):      # scelta primo e secondo
            l_max[i] = max(matrix[i])
            l_max_index[i] = matrix[i].index(max(matrix[i]))
        index_max_row = l_max.index(max(l_max))
        index_max_col = l_max_index[index_max_row]

        team.pizze.append(listaPizze[index_max_col].id)
        team.pizze.append(listaPizze[index_max_row].id)
        matrix[index_max_row][index_max_col] = -1

        #for i in range(COSTANTE):
        #    print(matrix[i])
        
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)

        for i in range(len(matrix)):        # mette -1 nelle celle scelte
            if i == index_max_col or i == index_max_row :
                matrix[i] = [-1 for x in range(COSTANTE)]
            else:
                for j in range(len(matrix[i])):
                    if j == index_max_col or j == index_max_row :
                        matrix[i][j] = -1

        pizze_scelte[index_max_col] = listaPizze[index]
        #pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[index_max_row] = listaPizze[index-1]
       # print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)

        #index += 2
        index = calcolaFineBlocco()-1
        #print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )

        #print(f'Numero di team: {len(listaTeam)}')
        numTeam2-=1

def riempiteam():
    #print(numTeam3)
    riempiteam4()
    riempiteam3()
    riempiteam2()

#######################################################################################################################################
totPizze = None
numTeam2 = None
numTeam3 = None
numTeam4 = None
listaTeam = []
listaPizze = []
numPizzeTotali = len(listaPizze)

#leggiFile('d_many_pizzas.in')
#leggiFile('b_little_bit_of_everything.in')
leggiFile('c_many_ingredients.in')
#leggiFile('e_many_teams.in')

riempiteam()

for t in listaTeam:
    t.stampa()

