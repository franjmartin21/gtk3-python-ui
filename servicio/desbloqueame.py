
class Desbloqueame:

    def __init__(self):
        '''
        Estos deberian de ser recuperados desde fichero
        '''
        self.coche_objetivo = 'H033'
        self.coches_estacionados = ['V542', 'V442', 'V103']

    def recuperar_coche_objectivo(self):
        return self.coche_objetivo

    def recuperar_coches_estacionados(self):
        return self.coches_estacionados


'''

COE = u'\u2500' # ─
CNS = u'\u2502' # │
CES = u'\u250C' # ┌
CSO = u'\u2510' # ┐
CNE = u'\u2514' # └
CON = u'\u2518' # ┘
COES = u'\u252C' # ┬
CNES = u'\u251C' # ├
CONS = u'\u2524' # ┤
CONE = u'\u2534' # ┴
CSOM = u'\u2593' # ▒

cva = CES+COE*3+CSO
cvi = CNS+" "*3+CNS
cvix = CNS+" "
cviy = " "+CNS
cvb = CNE+COE*3+CON

cha1 = CES+ COE*4
#chai = CNS+" "*4
chai = CNS+" "
cha2 = CNE+COE*4
chi = COE*5
chb1 = COE*4+CSO
#chbi = " "*4+CNS
chbi = " "+CNS
chb2 = COE*4+CON

emp= " "*5

cars = ['V112','H122','V233']
letmay = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
letmin = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}

let = ['A','B','C','D','E','F','G','H']
letmy = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
letmn = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
letras = [letmy,letmn]
boxval = [11,12,13,14,15,16,21,22,23,24,25,26,31,32,33,34,35,36,37,41,42,43,44,45,46,51,52,53,54,55,56,61,62,63,64,65,66]


matrix=[[0 for tr in range(6)]for tr in range(6)]


for e in range(4):
    li = [[[emp for t in range(3)] for s in range(6)]for u in range(6)]
    cont = 1
    for car in cars:
        print (car)
        tam = int(car[3:])
        box = int(car[1:3])
        dir = car[:1]
        print (box)
        i = int(box/10 -1)
        j = int(box%10 -1)
        print (i)
        print (j)
        if (dir == 'H'):
            li[i][j]=[cha1,chai+letmay[cont]+" "*2,cha2]
            for x in range(1,tam-1):
                li[i][j+x] = [chi,emp,chi]
            li[i][j+tam-1] = [chb1," "*2+letmin[cont]+chbi,chb2]

        elif (dir == 'V'):
            li[i][j]=[cva,cvix+letmay[cont]+cviy,cvi]
            for x in range(1,tam-1):
                li[i+x][j] = [cvi,cvi,cvi]
            li[i+tam-1][j] = [cvi,cvix+letmin[cont]+cviy,cvb]
        cont = cont +1

    print (CES+(COES+COE*4)*6+CSO)
  
    for i0 in (0,1,2,3,4,5):
        for k0 in (0,1,2):
            if (k0==0):
                print (CNES,end=" ")
            else:
                print (CNS, '')

            for j0 in (0,1,2,3,4,5):
                print (li[i0][j0][k0], '')

            if (i0 == 2):
                print (CSOM)
            elif (k0==0):
                print (CONS)
            else:
                print (CNS)
    print (CNE+(CONE+COE*4)*6+CON)

    ms = input('Mover?')
    ms = str(ms)
    mlen = len(ms)
    for it in range(mlen):
        m = ms[it-1:it+1]
        where = 1
        for t in range(8):
            if (m == let[t-1]):
                where = 0

        carnum = int(letras[where][m]) - 1
        car = cars[carnum]
        tam = int(car[3:])
        box = int(car[1:3])
        dir = car[:1]
        if (dir == 'H'):
            if (where == 0):
                box2 = box-1
                cars[carnum] =str(dir + str(box2) + str(tam))

            else:
                box2 = box+1
                cars[carnum] =str(dir + str(box2) + str(tam))

        elif (dir == 'V'):
            if (where == 0):
                box2 = box-10
                cars[carnum] =str(dir + str(box2) + str(tam))

            else:
                box2 = box+10
                cars[carnum] =str(dir + str(box2) + str(tam))
print ('end')
'''
def pintar_algo():
    print('Algo')