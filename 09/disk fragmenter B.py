filnavn = "eks1.txt"
# filnavn = "input.txt"

with open(filnavn) as fil:
    linje = [int(i) for i in fil.readline().strip()]
print(linje)

disk = []
indeks = -1
fil = 0
# empty = {
#                     "ID":-1,
#                     "rep":"."
#                 }
# for tall in linje:
#     fil = not fil
#     if fil:
#         indeks+=1
#         for _ in range(tall):
#             disk.append(
#                 {
#                     "ID":indeks,
#                     "rep":str(indeks)[0],
#                     "len":tall
#                 }
#             )
            
#     else:
#         for _ in range(tall):
            
#             disk.append(
#                 {
#                     "ID":-1,
#                     "rep":".",
#                     "len":tall
#                 }
#             )
            



def visDisk(liste):
    
    for i in liste[0].keys():
        print(f"{i:3}",end=" : ")
        for info in liste:
            print(f"{info[i]:>3}",end="")
        print()
    print()
    

# visDisk(disk)
#Prøver en annen fremgangsmåte
# Vi vet vi har annenhver tall for fil og åpenrom. Vi legger inn en struktur for hver av disse slik:

fil = False
for tall in linje:
    fil = (fil +1) %2 
    if tall == 0:
        continue
    if fil: indeks+=1
    disk.append(
                    {
                "fil": fil,
                "ID": indeks if fil else "-1",
                "len": tall
            }
    )

visDisk(disk)
# Om vi flytter den så må vi: flytte frem fila, og muligens fjerne den tomme
i=0
j=len(disk)-1

while i <= j:
    
    v = disk[i]
    h = disk[j]

    if v["fil"]:
        i+=1
    elif not h["fil"]:
        j-=1
    elif v["len"] >= h["len"]:
        disk.insert(i,disk.pop(j))
        v["len"] -= h["len"]
        if v["len"] <= 0:
            disk.pop(i+1)
        disk.insert(j,)
        print("Alt 1")
        visDisk(disk)
    else:
        # Da har vi v:åpen, h: fil, men h er større enn v. Så må loope igjennom og sjekke om det er noen v større enn h, og så flytte som ovenfor -_-
        n = i 
        
        funnet = False
        while not funnet and n<j:
            t = disk[n]
            if not t["fil"] and t["len"]>=h["len"]:
                funnet=True
            else:
                n+=1
        if funnet:
            disk.insert(n,disk.pop(j))
            t["len"] -= h["len"]
            if t["len"] <= 0:
                disk.pop(n+1)
                
            print("Alt 2")
            visDisk(disk)
        else:
            print(f"flyttet ikke {i,j} - {h}")
            j-=1

# flytt filer
# i = 0
# j = len(disk)-1
# while i <= j:
#     lengdeFlytt= disk[j]["len"] 

#     if disk[i]["ID"]!=-1:
#         i += disk[i]["len"]
#     elif disk[j]["ID"]!=-1:
#         # om i er tom og j ikke er det: 
#         neste = i
#         nesteLen=disk[neste]["len"]
#         while  nesteLen< lengdeFlytt or neste > j:
#             neste += nesteLen
#             # Kan hoppe et helt steg fremmover
        
#         if disk[neste]["len"] >= lengdeFlytt:
#             # Fant et ledig rom #TODO flytte fila og oppdatere ledig rom
#             visDisk(disk)
#             # print(i,j,neste, lengdeFlytt)
#             for k in range(lengdeFlytt):
#                 # print(k, neste+k, j-k)
#                 print("i",i,"j",j, "neste", neste, disk[neste]["len"])
#                 print("flytter", disk[j])
#                 disk[neste+k],disk[j-k] = disk[j-k],disk[neste+k]
#             if nesteLen < lengdeFlytt:
#                 for k in range(neste+nesteLen, neste + lengdeFlytt):
#                     disk[k]["len"] = disk[k]["len"] - lengdeFlytt

#             j -= lengdeFlytt   
#     else:
#         j-=1

visDisk(disk)
løsning = 0 
for i in range(len(disk)):
    if disk[i]["ID"]!= -1:
        løsning+= i * disk[i]["ID"]
print(løsning)