from time import time

def compare(l1,l2):
    return list(set(l1) & set(l2))!=[]

def code(file):
    f1 = open(file, 'r', encoding='UTF-8')
    tags = {}   #id: [tags]
    d = {}  #id: [v/h, n_tags]
    n_photos = int(f1.readline())
    i = 0
    for r in f1:
        r = r.strip().split()
        d[i] = [r[0], int(r[1])]   #[v/h, n_tags]
        r.pop(0)
        r.pop(0)
        tags[i] = r
        i+=1
    d_copy = d.copy()
    complete = False
    len_d = i
    print(len_d)
    i = 0
    final = []
    black_list = []
    start = time()
    final_tag = []
    v = False
    while complete == False:
        while(i not in d and time()-start<30):
            i+=1
        if time()-start>30:
            break
        if(len(black_list)>=len_d):
            complete = True
            break
        if i==len_d:
            i=0
        if i in black_list:
            i+=1
            continue
        if len(final)==0:
            final.append(i)
            black_list.append(i)
            final_tag = tags[final[-1]]
            d.pop(i, None)
            tags.pop(i, None)
            i+=1
            continue
        if  d[i][0] == 'H' and compare(tags[i], final_tag):
            final.append(i)
            black_list.append(i)
            final_tag = tags[final[-1]]
            d.pop(i, None)
            tags.pop(i, None)
            i+=1
            start = time()
            continue

        if  d[i][0] == 'V' and compare(tags[i], final_tag) and not v:
            final.append(i)
            black_list.append(i)
            final_tag = tags[final[-1]]
            d.pop(i, None)
            tags.pop(i, None)
            i+=1
            start = time()
            v = True
            continue

        if  d[i][0] == 'V' and compare(tags[i], final_tag) and v:
            final.append(i)
            black_list.append(i)
            final_tag = tags[final[-1]]
            d.pop(i, None)
            tags.pop(i, None)
            i+=1
            start = time()
            v = False
            continue

            #var = find_other_v(tags, i, d, black_list)
            #if var is not None:
            #    final.append(i)
            #    black_list.append(i)
            #    final_tag = tags[final[-1]]
            #    d.pop(i, None)
            #    tags.pop(i, None)
            #    final.append(var)
            #    black_list.append(var)
            #    final_tag = tags[final[-1]]
            #    d.pop(var, None)
            #    tags.pop(var, None)
            #    start = time()
            #i+=1
            #continue
        i+=1
        print('Lunghezza lista finale: ', len(final), '. Iteratore: ',i)
    print(len(final))
    return final, d_copy


def compare1(l1, l2):
    per = 0
    tot = len(l1)
    for elem in l1:
        if elem in l2:
            per+=1
    return round(100*per/tot)

#def find_other_v(tags, index, d, black_list):
#    for t in tags:
#        if t == index or t in black_list:
#            continue
#        if d[t][0]=='V' and compare(tags[t], tags[index]):
#            return t
#    return None
        
def results():
    res, d = code('b_lovely_landscapes.txt')
    tot = 0
    for r in res:
        if d[r][0] == 'H':
            tot += 1
        else:
            tot += 0.5
    f1 = open('b_results.txt', 'w', encoding='UTF-8')
    src = []
    val = None
    f1.write(str(int(tot)) + '\n')
    for riga in res:
        if d[riga][0] == 'H' and riga not in src:
            src.append(riga)
            f1.write(str(riga) + '\n')
        elif d[riga][0] == 'V' and riga not in src and val == None:
            val = riga
            src.append(str(riga))
        elif d[riga][0] == 'V' and riga not in src and val != None:
            f1.write(str(val) + ' ' + str(riga) + '\n')
            src.append(riga)
            val = None
    f1.close()
            


s = time()
results()
print('Tempo: ', round(time()-s, 3))

#print(code('a_example.txt'))
#print(code('b_lovely_landscapes.txt'))
#print(code('c_memorable_moments.txt'))
#print(code('d_pet_pictures.txt'))




