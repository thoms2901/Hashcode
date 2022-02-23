class Auto:
    def __init__(self, numStrade, listaStrade):
        self.numStrade = numStrade
        self.listaStrade = listaStrade

class Strada:
    def __init__(self, nome, inizio, fine, tempoPercorrenza):
        self.nome = nome
        self.inizio = inizio
        self.fine = fine
        self.tempoPercorrenza = tempoPercorrenza

class Incrocio:
    def __init__(self, id):
        self.id = id
        self.listaIn = []
        self.listaOut = []
        
    # def __eq__(self, other):
    #     if isinstance(other, Incrocio):
    #         return self.id == other.id
    #     return False


def leggiFile(file):
    global listaAuto
    global listaStrade
    global tempoTotale
    global numStrade
    global numIncroci
    global numAuto
    global bonus
    f = open(file, 'r', encoding='UTF-8')
    prima_riga = f.readline()
    tempoTotale, numIncroci, numStrade, numAuto, bonus = list(map(int, prima_riga.strip().split()))
    for i in range(numStrade):
        riga = f.readline().strip().split()
        incr_start = None
        incr_end = None
        # incr_start = Incrocio(int(riga[0]))
        # incr_end = Incrocio(int(riga[1]))
        i_s = False
        i_e = False
        for incrocio in listaIncroci:
            if i_s and i_e:
                break
            if incrocio.id == int(riga[0]) and not i_s:
                incr_start = incrocio
                i_s = True
            elif incrocio.id == int(riga[1]) and not i_e:
                incr_end = incrocio
                i_e = True
        if i_s == False:
            incr_start = Incrocio(int(riga[0]))
        if i_e == False:
            incr_end = Incrocio(int(riga[1]))
        if incr_start not in listaIncroci:
            listaIncroci.append(incr_start)
        if incr_end not in listaIncroci:
            listaIncroci.append(incr_end)
        street_name = riga[2]
        street_time = int(riga[3])
        strada = Strada(street_name, incr_start, incr_end, street_time)
        listaStrade.append(strada)
        incr_start.listaOut.append(strada)
        incr_end.listaIn.append(strada)
    for i in range(numAuto):
        riga = f.readline().strip().split()
        auto = Auto(int(riga.pop(0)), riga)
        listaAuto.append(auto)

    for i in listaIncroci:
        print(i.id)
    #emergency(file)



################################################################################
    # f = open('provac.txt', 'w')
    # f.write('Lista auto: \n\n')
    # for i in listaAuto:
    #     f.write(f'Auto con {i.numStrade}, e strade {i.listaStrade}')
    #     f.write('\n')
    # f.write('\nLista strade\n\n') 
    # for i in listaStrade:
    #     f.write(f' Strada {i.nome}, con tempo di percorrenza {i.tempoPercorrenza}, incorcio inizio con id {i.inizio.id}, incrocio fine con id {i.fine.id}')
    #     f.write('\n')
    # f.close()


def emergency(file):
    f = open(file[0] + '.out', 'w', encoding='UTF-8')
    n_incorci = len(listaIncroci)
    f.write(str(n_incorci) + '\n')
    print(n_incorci)
    for i in listaIncroci:
        id = i.id
        #print(id)
        f.write(str(id)+ '\n')
        n_streets = len(i.listaIn)
        f.write(str(n_streets) +'\n')
        #print(n_streets)
        for street in i.listaIn:
            #print(street.nome, ' 1')
            f.write(str(street.nome) +' 1\n')
    f.close()

def riavvia():
    listaAuto = []
    listaStrade = []
    listaIncroci = []
    tempoTotale = 0
    numStrade = 0
    numIncroci = 0
    numAuto = 0
    bonus = 0


listaAuto = []
listaStrade = []
listaIncroci = []
tempoTotale = 0
numStrade = 0
numIncroci = 0
numAuto = 0
bonus = 0


print('File a')
leggiFile('a.txt')
riavvia()
print('File b')
leggiFile('b.txt')
# riavvia()
# print('File c')
# leggiFile('c.txt')
# riavvia()
# print('File d')
# leggiFile('d.txt')
# riavvia()
# print('File e')
# leggiFile('e.txt')
# riavvia()
# print('File f')
# leggiFile('f.txt')

