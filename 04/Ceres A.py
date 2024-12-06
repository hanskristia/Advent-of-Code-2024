
filnavn = "eks1.txt"
filnavn = "input.txt"

with open(filnavn) as fil:

    data=[]
    for linje in fil:
        data.append(linje.strip())


print(data)
x_pos=[]
høyde = len(data)
lengde = len(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="X":
            x_pos.append((i,j))
print(x_pos)

# Jeg har nå alle x-posisjonene. 
# Da må jeg søkeigjennom de 8 mulige naboene for M
retninger = []
for i in range(-1,2):
    for j in range(-1,2):
        if i == 0 and j == 0:
            pass
        else:
            retninger.append((i,j))
print(retninger)

ord="XMAS"
def sjekkRetning(a,b,indeks,retning,høyde=høyde,lengde=lengde):
    if indeks > 3: 
        
        return True
    
    a += retning[0]
    b += retning[1]
    # print(a,b)
    if not any((min(a,b)<0, a >= høyde, b >= lengde)):
        
        if data[a][b] == ord[indeks]:
            # print(data[a][b])
            # print(a,b, retning)
            return(sjekkRetning(a,b,indeks+1,retning))
        else:
            # print(data[a][b], "-> stopper")
            pass
            
    return False
            
løsninger=0
for y,x in x_pos:
# for y,x in [(9,5)]:
    # print(y,x, "Sjekker rundt X; ")
    for retning in retninger:
        a,b = y,x
        # print("sjekker", retning)
        if sjekkRetning(a,b,1,retning):
            # print("fant ord")
            løsninger+=1
print(løsninger)
            

# For hver av disse retningene: Sjeke om AS er i samme retning


