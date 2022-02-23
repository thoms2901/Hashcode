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
    l_id_incroci = []
    for i in range(numStrade):
        riga = f.readline().strip().split()

        
        incr_start = None
        incr_end = None

        if int(riga[0]) in l_id_incroci:
            incr_start = listaIncroci[l_id_incroci.index(int(riga[0]))]
        else:
            incr_start = Incrocio(int(riga[0]))
            listaIncroci.append(incr_start)
            l_id_incroci.append(int(riga[0]))

        if int(riga[1]) in l_id_incroci:
            incr_end = listaIncroci[l_id_incroci.index(int(riga[1]))]
        else:
            incr_end = Incrocio(int(riga[1]))
            listaIncroci.append(incr_end)
            l_id_incroci.append(int(riga[1]))

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


def emergency(file):
    f = open(file[0] + '.out', 'w', encoding='UTF-8')
    n_incorci = len(listaIncroci)
    f.write(str(n_incorci) + '\n')
    print(n_incorci)
    for i in listaIncroci:
        id = i.id
        f.write(str(id)+ '\n')
        n_streets = len(i.listaIn)
        f.write(str(n_streets) +'\n')
        for street in i.listaIn:
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
riavvia()
print('File c')
leggiFile('c.txt')
riavvia()
print('File d')
leggiFile('d.txt')
riavvia()
print('File e')
leggiFile('e.txt')
riavvia()
print('File f')
leggiFile('f.txt')

