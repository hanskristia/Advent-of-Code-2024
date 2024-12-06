
filnavn = "eks2.txt"
filnavn = "input.txt"

with open(filnavn) as fil:

    data=[]
    for linje in fil:
        data.append(linje.strip())

# for linje in data:
#     print(linje)
a_pos=[]
høyde = len(data)
lengde = len(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="A":
            a_pos.append((i,j))
# print(a_pos)

# Jeg har nå alle A-posisjonene. 
# Da må jeg sjekke krysset for M & S samtidig
retninger = [(-1,-1),(-1,1)]

løsninger=0
for y,x in a_pos:
# for y,x in [(9,5)]:
    riktige=0
    for retning in retninger:
        diagonal=""
        for alt in [1,-1]:
            a,b = y,x
            a += alt*retning[0]
            b += alt*retning[1]
            # print(a,b)
            if not any((min(a,b)<0, a >= høyde, b >= lengde)):
                
                diagonal+=(data[a][b])
        if len(diagonal)==2:
            if diagonal in ("MS","SM"):
                riktige+=1
    if riktige==2:
        # print(y,x)
        løsninger+=1
print(løsninger) # 3523 too high
            

# For hver av disse retningene: Sjeke om AS er i samme retning

Myvar = 1
_myvar = 1
my-var = 1
my_var = 1
print(Myvar,_myvar,my-var, my_var)