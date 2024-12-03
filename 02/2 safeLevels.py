
def lesInput(filnavn)->list[str]:
    inputs:list[str] = []
    with open(filnavn) as fil:
        for linje in fil:
            inputs.append(linje)
    return inputs


def behandle_levels(levels:list[str]):
    antall=0
    res = []
    for level in levels:
        level.strip()
        res=[int(i) for i in level.split()]

        print(res)
        if erKorrekt(res):
            print("Er korrekt")
            antall+=1

    return antall

def erKorrekt(sjekk:list[int]):
    if not innenforListesjekk(sjekk):
        return False

    if sjekk[0]<sjekk[1]:
        if all([sjekk[i]<sjekk[i+1] for i in range(len(sjekk)-1)]):
            return True
    else:
        if all([sjekk[i]>sjekk[i+1] for i in range(len(sjekk)-1)]):
            return True
        
def innenforListesjekk(sjekk:list[int]):
    return all([innenforsjekk(sjekk[i],sjekk[i+1]) for i in range(len(sjekk)-1)])

def innenforListesjekkDemping(sjekk:list[int]):
    return [innenforsjekk(sjekk[i],sjekk[i+1]) for i in range(len(sjekk)-1)].count(False)

def innenforsjekk(a:int,b:int):
    
    if 1 <= abs(a-b) <= 3:
        return True
    else:
        return False

filnavn="ex1.txt"
filnavn="input.txt"
# 
# print(behandle_levels(lesInput(filnavn)))

levels = lesInput(filnavn)
safe = 0
res:list[list[int]] = []
for level in levels:
    level.strip()
    res.append([int(i) for i in level.split()])



# print(res)
# for linje in res:
#     økendeCheck=[1 if linje[i]<linje[i+1] else -1 for i in range(len(linje)-1)  ]
#     summering = sum(økendeCheck)
#     difsCheck = [ abs(linje[i]-linje[i+1]) <= 3 for i in range(len(linje)-1)] 
#     difs = difsCheck.count(False)

#     if abs(summering) <= (len(linje)-1)-4:
#         # print("sum;",summering, (len(linje)-1)-4, linje)
#         # To sett med tall er feil, kan ikke reddes
#         pass
#     elif difs>2:
#         # print("dif;" ,difsCheck, linje)
#         # Tre sett med tall er feil, kan derfor ikke reddes. Kan redde to
#         pass
#     elif difs == 0 and abs(summering) == len(linje)-1:
#         safe += 1
#     else:
#         indekserDifs = []
#         [ indekserDifs.append(i) if not difsCheck[i] else 0 for i in range(len(difsCheck))]
#         if not indekserDifs:
#             ## Da er det kun økning som er feil

#         print(linje, indekserDifs, difs, difsCheck)
    
   
#Bør ha annen angrepsmåte her. Kan nok sjekke rekursivt? 
## typ sjekk om linja er ok på begge. 
# Om den ikke er ok på en så øk endret med en og sjekk om denne lista er ok når vi har fjernet denne. 
# Om endret når 2 så returnerer vi false om ikke ok. 

def rekursivLøsning(linje:list[int],sjekk=0)-> bool:
    if sjekk > 1:
        return False
    økendeCheck=[1 if linje[i]<linje[i+1] else -1 for i in range(len(linje)-1)  ]
    summering = sum(økendeCheck)
    # Tror heller ingen falske positive på økende... Å nei...
    difsCheck = [ abs(linje[i]-linje[i+1]) <= 3 for i in range(len(linje)-1)]
    difs = difsCheck.count(False)
    # ingen falske positive på difs

    if difs == 0 and abs(summering)==len(linje)-1:
        return True
    else:
        
        for i,j in enumerate(difsCheck):
            if j: 
                a = linje.pop(i)
                if (rekursivLøsning(linje, sjekk+1)):
                    return True
                linje.insert(i,a)
        if summering >= 0 :
            for i,j in enumerate(økendeCheck):
                if j == -1:
                    a = linje.pop(i)
                    if (rekursivLøsning(linje, sjekk+1)):
                        return True
                    linje.insert(i,a)
        else:
            for i,j in enumerate(økendeCheck):
                if j == 1:
                    a = linje.pop(i)
                    if (rekursivLøsning(linje, sjekk+1)):
                        return True
                    linje.insert(i,a)
            
    return False

for linje in res:
    if rekursivLøsning(linje):
        if [ abs(linje[i]-linje[i+1]) <= 3 for i in range(len(linje)-1)].count(False):
            print("safe",linje, [ abs(linje[i]-linje[i+1]) <= 3 for i in range(len(linje)-1)].count(False))
        
        if sum([1 if linje[i]<linje[i+1] else -1 for i in range(len(linje)-1)  ]) >= 0:
            pass
        else:
            linje.reverse()
        if [linje[i]<linje[i+1] for i in range(len(linje)-1)].count(False) > len(linje)-2:
            print("safe",linje, [linje[i]<linje[i+1] for i in range(len(linje)-1)].count(False))

    
        safe+=1
    else:
        # print("unsafe",linje)
        pass
print(safe)

# 593 er for høyt, får altså falske positiver
# 461 Implementerte sjekk, er også for høyt