filnavn = "eks1.txt"
filnavn = "input.txt"
løsning = 0

def operations(resultat,svar,i,tallListe):
    # Slutt betingelser:
    if resultat == svar and i ==len(tallListe):
        
        # print()
        # print(f"{svar} ? {resultat}, dybde = {i}, \n {tallListe}. \n {løsning}")
        a = tallListe.pop(0)

        return True
    elif resultat > svar:
        # print("\t Ikke riktig, ble for høyt")
        return False
    elif i >= len(tallListe):
        # print("\t Ikke riktig, ble for lavt")
        return False
    
    tall = tallListe[i]
    i=i+1

    # nye_l_a = løsning.copy()
    # nye_l_a.append("+")
    a = operations(resultat+tall, svar, i, tallListe)

    # nye_l_b=løsning.copy()
    # nye_l_b.append("*")
    b = operations(resultat*tall,svar, i, tallListe )   
    
    # nye_l_c = løsning
    # nye_l_c.append("||")
    resultat = int( str(resultat)+str(tall))
    c = operations(resultat, svar, i , tallListe)
    return any((a,b,c))
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
        if operations(res,svar,1,tall):
            løsning+=svar
            print("løsning",i, svar)

            antLøsninger+=1
print(løsning)
print(antLøsninger)
## FRyktelig treg. Her kunne jeg nok ha pruna tidligere, men det går fint