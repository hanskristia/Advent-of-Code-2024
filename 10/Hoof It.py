filnavn = "eks1.txt" # 36
# filnavn = "eks3.txt" # 4
# filnavn = "eks4.txt" # 3
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
# Løsningstrategi: 
# Fra en og en start node:
# Bredde først søk etter økning på en. 
# Lagre informasjonen etter BFS på hver node på kartet, med tilbakepropagering. 
# Om jeg da senere kommer på inn på et sted med ferdige noder, så kan jeg klippe BFS fra da. 
# fattigmans Memoisering

def innenforKart(x,y):
    return  not( min(x,y) < 0 or y > høyde or x > lengde)

retninger = [(1,0),(-1,0),(0,1),(0,-1)]
åsjekke=[] # inputverdier for neste søk-kall

def leggTilRetninger(y,x,n):
    for retning in retninger:
        y_n,x_n = y+retning[0], x+retning[1]
        # print(f"{x_n} {y_n}")
        leggTilSøk(y_n,x_n,n)
    # print()
def leggTilSøk(y,x,n):
    if innenforKart(y,x):
        # print(f"er innenfor {y,x}")
        # print((y,x,n),end=",")
        åsjekke.append((y,x,n))        
        return True
    # print(f"er utenfor {y,x}")
    return False

def nesteSøk(s):
    if åsjekke:
        a = åsjekke.pop(0)
        # print(a)
        return søk(*a,s)
    else:
        print("Ferdig?")
    return s
def søk(y,x,n,s):
    # printKart(kart)
    # print(y,x,n)
    # print(åsjekke)
    if n == 9 and kart[y][x]==9:
        # print(f"fant ved {y} {x}")
        if (y,x) not in s:
            s.append((y,x))
    elif kart[y][x] == n:
        leggTilRetninger(y,x,n+1)
    return nesteSøk(s)
    # else: 
    #     return False
    ## Problem sjekker kun den første jeg finner. Må implementerre en stack for å kunne gjøre BFS.
    
    ## Forbedring sjekke om jeg har sett på ruta før? Altså om søket har vært positiv nå. Hvordan unngå å legge til unødvendige i sjekke bunken?

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
    
# printKart(kart)
# print(åsjekke)
ans = []
for y,x in start:
    temp = søk(y,x,0,[])
    # print(y,x)
    # print(temp)
    # print("antall noder:", len(temp))  
    ans.append(len(temp))            
            # Hvordan amoisere denne?
        # Har 9 noder, jeg finner kun 7. Men en start-
        # Ikke en start algon min er wildly feil... 
        # Finner alle 9'ere den møter på et vis... 
        # Og kan finne samme node flere ganger.
printKart(kart)
print(start)
print(ans)
print(sum(ans))
