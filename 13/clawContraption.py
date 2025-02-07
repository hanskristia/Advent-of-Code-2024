from math import gcd
filnavn="eks1.txt"
# Gir opp på denne, har ikke styr på mattematikken :| 
with open(filnavn) as fil:

    linjer = fil.readlines()
for i in range(0,len(linjer),4):
    opg=[]
    for j in range(0,3):
        a = linjer[i+j].split(":")[1].strip().split(",")
        if j < 2:
            a = [int(i.split("+")[1]) for i in a]
        else:
            a = [int(i.split("=")[1]) for i in a]
        opg.append(a)
    

    # Har nå en oppgave på formen [A,B,C], der A,B er knapp A,B x og y, og C er løsningen, xy 
    maksiterasjoner=100
    # print("Test mod")
    # print(opg)
    
    # a,b,c = opg
    # for i in range(100):
    #     for j in range(100-i):
    #         x = a[0]*i+b[0]*j
    #         y = a[1]*i+b[1]*j
    #         print(x,y,c)
    #         if any((x > c[0], y > c[1])):
    #             break
    #         elif x == c[0] and y == c[1]:
    #             print(i,j)
        
    # Denne algoritmen vil ha en fryktelig kjøretid på N*10^4 ...

#     # Euklids algoritme
# utregning=[]
# def euklidsAlgoritme(a,b)-> tuple:
#     temp = a%b
#     # a,b = 
#     print(f"{a}={a//b}*{b}+{a%b}")
#     if temp:
#         utregning.append((b,temp))
#         return(euklidsAlgoritme(b,temp))
#     else: 
#         # utregning.append((b,0))
#         return a,b
# # x,y=0,0    
# for bit in reversed(utregning):
#     pass

# # print(euklidsAlgoritme(a,b), gcd(a,b))
# print(utregning)
# # print(euklidsAlgoritme(94,22))
# # Strategi: Finn alle nA+mB som gir X0, sjekk om denne også gir X1. 
# # Alt strategi: Finn alle nA+mB som gir X0, og finn alle som gir X1 og sjekk om noen av disse er de samme. Bruke sett til dette?
# temp = gcd(a,b)
# if c % temp != 0:
#     print("ingen løsnning")
# else:
#     # gå baklengs igjennom euklids
#     pass

def solve_Dioph(a,b,c):
    m1=1
    m2=0
    n1=0
    n2=1
    r1=a
    r2=b
    while r1%r2!=0:
        q=r1//r2
        aux=r1%r2
        r1=r2
        r2=aux
        aux3=n1-(n2*q)
        aux2=m1-(m2*q)
        m1=m2
        n1=n2
        m2=aux2
        n2=aux3
    return m2*c,n2*c
a,b,c = 94,22,8400
a,b,c = 321,78,3
print(solve_Dioph(a,b,c)) # Får en løsning..  