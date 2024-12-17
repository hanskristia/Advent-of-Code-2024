filnavn = "input.txt"

kart:list[list[int]] = []
start:list[tuple[int,int]] = []
with open(filnavn) as fil:
    y = -1
    for linje in fil:
        y+=1
        rad = []
        x=-1
        for i in linje.strip():
            x+=1
            if i != ".":
                rad.append(int(i))
            else:
                rad.append(-1)
            if i == "0":
                start.append((y,x))
        kart.append(rad)
høyde = y
lengde = x

def innenforKart(x,y):
    return  not( min(x,y) < 0 or y > høyde or x > lengde)

retninger = [(1,0),(-1,0),(0,1),(0,-1)]
åsjekke=[] # inputverdier for neste søk-kall

def leggTilRetninger(y,x,n):
    for retning in retninger:
        y_n,x_n = y+retning[0], x+retning[1]

        leggTilSøk(y_n,x_n,n)

def leggTilSøk(y,x,n):
    if innenforKart(y,x):
        åsjekke.append((y,x,n))        

def søk():
    y,x,n = åsjekke.pop(0)
    if n == 9 and kart[y][x]==9:
        return 1
    elif kart[y][x] == n:
        leggTilRetninger(y,x,n+1)
    return 0

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
ans = 0
for y,x in start:
    åsjekke=[]
    s=0
    leggTilSøk(y,x,0)
    while åsjekke:
        s+=søk()
    ans+=s
print(ans)