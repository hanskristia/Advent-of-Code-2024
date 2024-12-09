filnavn = "eks1.txt"
# filnavn = "input.txt"
løsning = 0

def multOrAdd(resultat,svar,i,tallListe, løsning:list):
    # Slutt betingelser:
    if resultat == svar and i ==len(tallListe):
        
        # print()
        # print(f"{svar} ? {resultat}, dybde = {i}, \n {tallListe}. \n {løsning}")
        a = tallListe.pop(0)
        for i,j in zip(tallListe,løsning):
            # print (f"{a} {j} {i} = ", end="")
            if j =="*":
                
                a*=i
            else:
                a+=i
            # print(a)
        if not a == resultat:
            print("DENNNE ", a, resultat)
        # print(a==resultat)
        return True
    elif resultat > svar:
        # print("\t Ikke riktig, ble for høyt")
        return False
    elif i >= len(tallListe):
        # print("\t Ikke riktig, ble for lavt")
        return False
    
    tall = tallListe[i]
    i=i+1

    nye_l_a = løsning.copy()
    nye_l_a.append("+")
    a = multOrAdd(resultat+tall, svar, i, tallListe,nye_l_a)

    nye_l_b=løsning
    nye_l_b.append("*")
    b = multOrAdd(resultat*tall,svar, i, tallListe,nye_l_b )   
  
    return a or b 
antLøsninger=0

with open(filnavn) as fil:
    # for i in range(100):
    #     linje=fil.readline()
    i=-1
    for linje in fil:
        i+=1
        # behandler input
        svar, tall = linje.strip().split(":")
        tall = [int(i) for i in tall.strip().split(" ")]
        svar = int(svar)
        # print(svar,tall)
        # Nå må jeg søke nedover i mulige løsninger, enten mult eller add. Kan gjøre dette rekursivt?
        res = tall[0]
        if multOrAdd(res,svar,1,tall,løsning=[]):
            løsning+=svar
            print("løsning",i, svar)

            antLøsninger+=1
print(løsning) 
print(antLøsninger)