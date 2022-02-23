class Pizza:
    def __init__(self,i_d, num_ing ,lista_ing):
        self.id = i_d
        self.numIng = num_ing
        self.listaIng = lista_ing
    
    def getId(self):
        return self.id
    
    def getNumIng(self):
        return self.numIng
    
    def getListaIng(self):
        return self.listaIng

    def __et__(self,p):
        return self.numIng < p.getNumIng()
    
    def __le__(self,p):
        return self.numIng <= p.getNumIng()
    def __gt__(self, p):
        return self.numIng > p.getNumIng()

    def __ge__(self, p):
        return self.numIng >= p.getNumIng()
    def unione(self, p):
        return len(set(self.listaIng) | set(p.listaIng))


class Team:
    def __init__(self, num):
        self.num = num
        self.pizze = []



def calcolaFineBlocco():
    global numTeam4
    global numTeam3
    global numTeam2
    global numPizzeTotali
    numPizzeTotali = len(listaPizze)
    if numTeam4>0 and numPizzeTotali>=4:
        return min(8,numPizzeTotali-1)
    elif numTeam3>0 and numPizzeTotali>=3:
        return min(6,numPizzeTotali-1)
    elif numTeam2>0 and numPizzeTotali>=2:
        return min(4,numPizzeTotali-1)
    else:
        return 0

def generaOutput(fileName):
    s = fileName[:-2]+"out"
    file = open(s, "w", encoding = "UTF-8")
    global listaTeam
    global numTeam2
    global numTeam3
    global numTeam4
    numTeamNonUsati = numTeam2+ numTeam3+ numTeam4
    global numTeamTotali
    file.write(str(len(listaTeam))+"\n")
    #file.write(str(numTeamTotali-numTeamNonUsati)+"\n")
    for team in listaTeam:
        riga = ""
        for i in team.pizze:
            #print(i)
            riga+=" "
            riga+=str(i)
            
        file.write("\n"+str(team.num)+riga)
    file.close()
    return

def leggiFile(file):
    f = open(file, "r", encoding = "UTF-8").readlines()
    info = f[0]
    info = info.strip().split()
    global listaPizze
    global numPizzeTotali
    numPizzeTotali = int(info[0])
    global numTeam2
    numTeam2 = int(info[1])
    global numTeam3
    numTeam3 = int(info[2])
    global numTeam4
    numTeam4 = int(info[3])
    listaTemp = []
    indice = 0
    global numTeamTotali
    numTeamTotali = numTeam2+numTeam3+numTeam4
    for riga in f:
        if riga == f[0]:
            continue
        else:
            riga = riga.strip().split()
            #p = Pizza(i_d, num_ing ,lista_ing)
            p = Pizza(indice,int(riga[0]),riga[1:])
            listaPizze.append(p)        
        indice+=1
    listaPizze.sort(reverse=True)
    return


def riempiteam4():
    global listaPizze
    global numTeam4
    n_team = numTeam4

    index = calcolaFineBlocco()-1
    COSTANTE = index
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
    
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]

    NUMERO_PIZZE_RICHIESTE = 4
    indici_scelti = []
    while numTeam4>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE:
        team = Team(4) #########
        listaTeam.append(team)
        if len(listaPizze) <= 7:
            team.pizze.append(listaPizze[0:4])
            listaPizze = listaPizze[4:]
            #print(listaPizze)
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
        #print(listaPizze[quarto_index])
        
        # indici_scelti.append(index_max_col)
        # indici_scelti.append(index_max_row)
        # indici_scelti.append(terzo_index)
        # indici_scelti.append(quarto_index)

        for i in range(len(matrix)):        # mette -1 nelle celle scelte
            if i == index_max_col or i == index_max_row or i == terzo_index or i == quarto_index:
                matrix[i] = [-1 for x in range(COSTANTE)]
            else:
                for j in range(len(matrix[i])):
                    if j == index_max_col or j == index_max_row or j == terzo_index or j == quarto_index:
                        matrix[i][j] = -1

        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)
        listaPizze.pop(terzo_index)
        listaPizze.pop(quarto_index)
        index = calcolaFineBlocco()-1
        #print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )
        pizze_scelte[index_max_col] = listaPizze[index]
        pizze_scelte[index_max_row] = listaPizze[index-1]
        #pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[terzo_index] = listaPizze[index-2]
        #pizze_scelte[terzo_index] = listaPizze[index+2]
        pizze_scelte[quarto_index] = listaPizze[index-3]
        #pizze_scelte[quarto_index] = listaPizze[index+3]
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)
        indici_scelti.append(quarto_index)

        

        #index += 4 #####
        index = calcolaFineBlocco()-1

        
        numTeam4-=1
###################################################################################################################
def riempiteam3():
    global listaPizze
    global numTeam3
    n_team = numTeam3
    index = calcolaFineBlocco()-1
    if len(listaPizze)<3:
        return
    COSTANTE = index ##
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
   
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]
    #print(pizze_scelte)
    NUMERO_PIZZE_RICHIESTE = 3
    indici_scelti = []
    
    while numTeam3>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE:
        team = Team(3)
        listaTeam.append(team)

        if len(listaPizze)==3:
            team.pizze = listaPizze
            listaPizze = []
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
        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)
        listaPizze.pop(terzo_index)
        index = calcolaFineBlocco()-1

        pizze_scelte[index_max_col] = listaPizze[index]
        pizze_scelte[index_max_row] = listaPizze[index-1]
        #pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[terzo_index] = listaPizze[index-2]
        #pizze_scelte[terzo_index] = listaPizze[index+2]
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        indici_scelti.append(terzo_index)
        

        #index += 3
        index = calcolaFineBlocco()-1
       # print(f'Numero di team: {len(listaTeam)}')
        numTeam3-=1
###################################################################################################################
def riempiteam2():
    global listaPizze
    global numTeam2
    n_team = numTeam2
    index = calcolaFineBlocco()-1
    if len(listaPizze)<2:
        return
    COSTANTE = index
    matrix = [[0 for x in range(COSTANTE)] for k in range(COSTANTE)]
    
    #pizze_scelte = listaPizze[0:index]
    pizze_scelte = [listaPizze[x] for x in range(COSTANTE)]
    #print(pizze_scelte)
    NUMERO_PIZZE_RICHIESTE = 2
    indici_scelti = []
    while numTeam2>0 and len(listaPizze)>=NUMERO_PIZZE_RICHIESTE and len(listaPizze)>=index:
        team = Team(2)
        listaTeam.append(team)
        if len(listaPizze)==2:
            team.pizze = listaPizze
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
        

        listaPizze.pop(index_max_col)
        listaPizze.pop(index_max_row)

        index = calcolaFineBlocco()-1
        #print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )
        pizze_scelte[index_max_col] = listaPizze[index]
        #pizze_scelte[index_max_row] = listaPizze[index+1]
        pizze_scelte[index_max_row] = listaPizze[index-1]
       
        indici_scelti.append(index_max_col)
        indici_scelti.append(index_max_row)
        

        #index += 2
        index = calcolaFineBlocco()-1
        #print(f'Indice: {index}, lunghezza lista: {len(listaPizze)}' )

        #print(f'Numero di team: {len(listaTeam)}')
        numTeam2-=1
###################################################################################################################
def riempiteam():
    #print(numTeam3)
    riempiteam4()
    riempiteam3()
    riempiteam2()


def start(fileName):
    global listaPizze
    global numPizzeTotali
    global numTeam2
    global numTeam3
    global numTeam4
    global listaTeam
    leggiFile(fileName)
    numTeamTotali = numTeam2+numTeam3+numTeam4
    riempiteam()
    generaOutput(fileName)
    return

#Main principale
def riavvia_variabili():
    global listaPizze
    listaPizze = []
    global numPizzeTotali
    numPizzeTotali = 0
    global numTeam2
    global numTeam3
    global numTeam4
    numTeam2 = 0
    numTeam3 = 0
    numTeam3 = 0
    global numTeamTotali
    numTeamTotali = 0
    global listaTeam
    listaTeam = []

listaPizze = []
numPizzeTotali = 0
numTeam2 = 0
numTeam3 = 0
numTeam4 = 0
numTeamTotali=0
listaTeam = []

print ("Esecuzione: "+"a_example")
start("a_example.in")
riavvia_variabili()
print ("Esecuzione: "+"b_little_bit_of_everything.in")
riavvia_variabili()
start("b_little_bit_of_everything.in")
print ("Esecuzione: "+"c_many_ingredients.in")
riavvia_variabili()
start("c_many_ingredients.in")
print ("Esecuzione: "+"d_many_pizzas.in")
riavvia_variabili()
start("d_many_pizzas.in")
print ("Esecuzione: "+"e_many_teams.in")
riavvia_variabili()
start("e_many_teams.in")
    



