filnavn = "eks1.txt"
filnavn = "input.txt"

pebbles = {}

def settIn(tall,ordbok,antall=1):
    if tall in ordbok:
        ordbok[tall]+=antall
    else:
        ordbok[tall]=antall

with open(filnavn) as fil:
    for s in fil.readline().split():
        settIn(int(s),pebbles)

print(pebbles)

def blinkAll(pebbles):
    nyDict={}
    for stein,antall in pebbles.items():
        if stein == 0:
            settIn(1,nyDict,antall)
        elif len(str(stein))%2==0:
            s=str(stein)
            l = len(s)//2
            a,b = s[:l],s[l:]
            # print(a,b,antall)
            settIn(int(a),nyDict,antall)
            settIn(int(b),nyDict,antall)
        else:
            settIn(stein*2024,nyDict,antall)
    return nyDict
for i in range(75):
    pebbles=blinkAll(pebbles)
    # print(pebbles)
    # print(sum(pebbles.values()))

print(sum(pebbles.values()))
# print(len("1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32".split(" ")))