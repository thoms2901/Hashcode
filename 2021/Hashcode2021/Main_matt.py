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
        self.numAutoTotali = 0
    def __gt__(self,y):
        return self.numAutoTotali>y.numAutoTotali


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
    for i in range(numStrade):
        riga = f.readline().strip().split()
        incr_start = Incrocio(int(riga[0]))
        incr_end = Incrocio(int(riga[1]))
        i_s = False
        i_e = False
        for incrocio in listaIncroci:
            if i_s and i_e:
                break
            
            if incrocio.id == incr_start.id and not i_s:
                incr_start = incrocio
                i_s = True
            elif incrocio.id == incr_end.id and not i_e:
                incr_end = incrocio
                i_e = True
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
        #aggiungo l'auto su ogni strada in cui passa
        for s in riga:
            strada = trovaStrada(str(s))
            strada.numAutoTotali+=1
   

  
schedule={}
listaAuto = []
listaStrade = []
listaIncroci = []
tempoTotale = 0
numStrade = 0
numIncroci = 0
numAuto = 0
bonus = 0


def trovaStrada(nome):
    for s in listaStrade:
        if s.nome==nome:
            return s

def setSemafori():
    global listaIncroci
    global schedule
    numstrade = 0
    n = 0
    listatuple = []
    for incrocio in listaIncroci:
        #incrocio.listaIn.sort()
        
        #levo le strade che hanno 0 macchine
        for strada in range(len(incrocio.listaIn)):
            if incrocio.listaIn[strada].numAutoTotali == 0:
                incrocio.listaIn[:strada]
                break
        #levo i semafori con solo strade con nessuna macchina
        if len(incrocio.listaIn)==0:
            continue
        #assegno i secondi di verde
        n = 1
        
        for s in incrocio.listaIn:
            tupla = (s,n)
            listatuple.append(tupla)
            schedule[incrocio.id] = listatuple
            
            
        listatuple = []

def generaOutput(nomeFile):

    global schedule
    nuovoNome = nomeFile[:-4]
    f_o = open(nuovoNome + "Out.txt","w",encoding="utf-8")
    numIntSched = len(schedule)
    f_o.write(str(numIntSched)+"\n")
    for key in schedule:
        streets = len(schedule[key])
        f_o.write(str(key) + "\n" )
        f_o.write(str(streets) + "\n")
        for i in range(streets):
            incrocio = schedule[key]
            riga = incrocio[i]
            f_o.write(str(riga[0].nome)+" "+ str(riga[1]) + "\n")


    f_o.close()

def start(fileName):
    leggiFile(fileName)
    setSemafori()
    generaOutput(fileName)
    return

# print("Esecuzione: a.txt" )
# start("a.txt")
 
# schedule={}
# listaAuto = []
# listaStrade = []
# listaIncroci = []
# tempoTotale = 0
# numStrade = 0
# numIncroci = 0
# numAuto = 0
# bonus = 0
# print("Esecuzione: b.txt" )
# start("b.txt")
 
# schedule={}
# listaAuto = []
# listaStrade = []
# listaIncroci = []
# tempoTotale = 0
# numStrade = 0
# numIncroci = 0
# numAuto = 0
# bonus = 0
# print("Esecuzione: c.txt" )
# start("c.txt")
 
schedule={}
listaAuto = []
listaStrade = []
listaIncroci = []
tempoTotale = 0
numStrade = 0
numIncroci = 0
numAuto = 0
bonus = 0
print("Esecuzione: d.txt" )
start("d.txt")
 
# schedule={}
# listaAuto = []
# listaStrade = []
# listaIncroci = []
# tempoTotale = 0
# numStrade = 0
# numIncroci = 0
# numAuto = 0
# bonus = 0
# print("Esecuzione: e.txt" )
# start("e.txt")
 
# schedule={}
# listaAuto = []
# listaStrade = []
# listaIncroci = []
# tempoTotale = 0
# numStrade = 0
# numIncroci = 0
# numAuto = 0
# bonus = 0
# print("Esecuzione: f.txt" )
# start("f.txt")