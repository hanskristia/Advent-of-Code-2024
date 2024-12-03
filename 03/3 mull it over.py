# Her er det kanskje reg-ex som er veien å gå? Men kan løse med annen Python.
import re
filnavn = "input.txt"
# A
# filnavn = "eks1.txt"
# løsning=0
# with open(filnavn) as fil:
#     for linje in fil:
#         for resultat in re.finditer("mul\([0-9]+,[0-9]+\)",linje):
            
#             a,b=resultat.strip("mul()").split(",")
#             a,b=int(a),int(b)
#             løsning+= a*b
# B
# filnavn = "eks2.txt"
løsning=0

def trim(sortert_liste,mål):
    while sortert_liste and sortert_liste[0] < mål:
        # print(sortert_liste,mål)
        
        sortert_liste.pop(0)

def trim_prosess(sortert_liste,mål):
    res=[]
    while sortert_liste and sortert_liste[0] < mål:
        res.append(sortert_liste.pop(0))
    return res

with open(filnavn) as fil:
    løsning = 0
    for linje in fil:
    # linje=next(fil)
    # if linje:
        dos = [i.start() for i in re.finditer("do\(\)",linje)]
        donts =  [i.start() for i in re.finditer("don't\(\)",linje)]
        mul = re.finditer("mul\([0-9]+,[0-9]+\)",linje)
        mul_starts =[]
        mults = []
        for i in mul:
            mul_starts.append(i.start())
            mults.append(i.group())
        mult_start = mul_starts.copy()
        debug = True


        
        if debug:
            print("  Dos:", dos)
            print("Donts:", donts)
            print("mults:", mul_starts)
            print("mults:", mults)

        indeks = 0
        do=0
        
        gyldige = []
        while True:
            if debug:
                print("steg 1")
                print("  Dos:", dos)
                print("Donts:", donts)
                print("gyldige",gyldige)
                print("multStart:", mul_starts)
            if donts:
                dont = donts.pop(0)
                if debug:
                    print("fjerner fra dos frem til ", dont)
                # Fjerner overflødige do, slik at vi ikke bytter for tidlig
                trim(dos,dont)
                # prosseserer opp til dont
                gyldige.extend(trim_prosess(mul_starts,dont))
            else:
                gyldige.extend(mul_starts)
            if debug:
                print("steg 2")
                print("  Dos:", dos)
                print("Donts:", donts)
                print("gyldige",gyldige)
                print("multStart:", mul_starts)
            
            if dos:
                do = dos.pop(0)
                if debug:
                    print("fjerner fra mul_starts frem til ", do)
                trim(mul_starts,do)

                if donts:
                    if debug:
                        print("fjerner fra donts frem til ", do)
                    trim(donts,do)
                
            else:
                break  
        # print(mult_start)
        if debug:print(gyldige)
        for i in gyldige:
            j=mult_start.index(i)
            resultat = mults[j]
            a,b=resultat.strip("mul()").split(",")
            a,b=int(a),int(b)
            løsning+= a*b
        if debug:
            print(løsning)
        if input():
            pass
print(løsning) 
#82552468 er for lavt.
#92974346 er for høyt. 
"""        # while donts:
        #     ## Prosesser alle mellom do og nest dont.
        #     dont = donts.pop(0)
        #     print(f"fra {do} til {dont}")
        #     while mul_starts[indeks] < dont:
        #         print(indeks)
        #         print(mul_starts[indeks])
        #         print(mults[indeks])
        #         a,b=mults[indeks].strip("mul()").split(",")
        #         a,b=int(a),int(b)
        #         løsning+= a*b
        #         indeks += 1
        #     # Finner neste do    
            
        #     while do < dont and dos:
        #         do = dos.pop(0)
        #     print(f"Ny do {do}")    
        # print(løsning)

        # enabled = True
        # next_dont = dont.pop(0)
        # while indeks < len(mults):
        #     start = mul_starts(indeks)
        #     if enabled:
        #         if start < next_dont:
        #             a,b=mults[indeks].strip("mul()").split(",")
        #             a,b=int(a),int(b)
        #             løsning+= a*b 
        #         else:
        #             enabled = False
        #             next_do = do.pop(0)
        #     else: 
        #         if start > next_do:
        #             enabled = True
        #             next_dont = dont.pop(0)
        #     indeks+=1
        
        # for neste in mul:
        #     pos = neste.start()
        #     if enabled:
        #         print(neste.group())
        #         a,b=neste.group().strip("mul()").split(",")
        #         a,b=int(a),int(b)
        #         løsning+= a*b 
"""
