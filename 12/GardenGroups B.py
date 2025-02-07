filnavn = "eks1.txt" # 80 ok
filnavn = "eks2.txt" # 1206 uok
# filnavn = "eks3.txt" # 236 ok 
# filnavn = "eks4.txt" # 368 uok

# filnavn = "input.txt"

kart:list[list[int]] = []


with open(filnavn) as fil:
    y = -1
    for linje in fil:
        y+=1
        rad = []
        x=-1
        for i in linje.strip():
            x+=1
            rad.append(i)
        kart.append(rad)
høyde = y
lengde = x

def innenforKart(x,y):
    return  not( min(x,y) < 0 or y > høyde or x > lengde)

def printKart(kart):
    print("    ",end="")
    for i in list(range(len(kart[0]))):
        print(f"{i:^3}" ,end="")
    print()
    print()
    
    for i,linje in enumerate(kart):
        print(i," ", end="")
        for j in linje:
            print(f"{j:>3}",end="")
        print()

retninger = [(1,0),(-1,0),(0,1),(0,-1)]

def likeNaboer(x:int,y:int)->int:
    # if not innenforKart(x,y):
    #     return -1 #??
    ant = 0
    val = kart[y][x]
    for i in retninger:
        
        y_0,x_0 = y+i[0], x+i[1]
        if innenforKart(x_0,y_0) and kart[y_0][x_0]==val:
            ant+=1 # Dette kan nok løses bedre med en liste itterasjon?
    return ant

def finnNaboer(kart):
    naboer=[]
    for i in range(len(kart)):
        temp = []
        for j in range(len(kart[0])):
            temp.append(likeNaboer(j,i))
        naboer.append(temp)
    return naboer


naboer = finnNaboer(kart)

retninger = [(1,0),(-1,0),(0,1),(0,-1)]
def sjekkNaboer(liste,sjekket,y,x,target,curr)->list:
    # printKart(sjekket)
    
    for ret in retninger:
        y_0,x_0 = y+ret[0], x+ret[1]
        if not innenforKart(x_0,y_0):
           
            continue

        if sjekket[y_0][x_0]:

            continue

        if liste[y_0][x_0] == target:

            sjekket[y_0][x_0] = True
            curr.append((y_0,x_0))
            sjekkNaboer(liste,sjekket,y_0,x_0,target,curr)
    return curr
        
def finnGrupper(liste):
    sjekket = [[False for j in range(len(liste[0]))]  for i in range(len(liste))]
    grupper = []
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            if not sjekket[i][j]:
                sjekket[i][j]=True
                grupper.append(sjekkNaboer(kart,sjekket,i,j,kart[i][j],[(i,j)]))
    return grupper


def prisGruppe(gruppe:list[tuple]):
    # print(kart[gruppe[0][0]][gruppe[0][1]],gruppe) 
    
    areal = len(gruppe)
    hjørner = 0
    for koord in gruppe:
        i,j = koord
        n = naboer[i][j]
        if n == 0:
            hjørner+=4
        elif n == 1:
            hjørner +=2 
        elif n == 3:
            hjørner += 2
        elif n == 2:
            nære = []
            for a,b in gruppe:
                if abs(a-i)+abs(b-j)==1:
                    nære.append((a,b))

            if nære[0][0] == nære[1][0] or nære[0][1] == nære[1][1]:
                # print(f"{i},{j} på linje")
                hjørner+=0
            else:
                # print(f"{i},{j} diagonalt")
                # print(nære)
                difs = [(i-a,j-b) for a,b in nære]
                y,x = 0,0
                for a,b in difs:
                    y-=a
                    x-=b 
                # print(f"difs: {(y,x)}")
                # print((i+y,j+x))
                if (i+y,j+x) in gruppe:
                    # print(" åpent tverss")
                    hjørner+=1
        
                else:
                    # print(" lukket tverss")
                    hjørner += 2
            
            
    print(f"{kart[gruppe[0][0]][gruppe[0][1]]}: A{areal},S{hjørner}, P: {areal*hjørner}")
    return areal * hjørner


res = 0
for gruppe in finnGrupper(kart):
    res += prisGruppe(gruppe)
print(res)
# Trenger en annen måte å gjøre det på. Usikker på når er det vi egt lager en ny side