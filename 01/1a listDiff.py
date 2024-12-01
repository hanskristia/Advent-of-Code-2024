
def lesInput(filnavn)->list[str]:
    inputs:list[str] = []
    with open(filnavn) as fil:
        for linje in fil:
            inputs.append(linje)
    return inputs

def behandle1a(inputs:list[str])->int:
    left = []
    right = []
    difs = []
    for inn in inputs:
        a,b = (int(i) for i in inn.strip().split())
        left.append(a)
        right.append(b)

    left.sort()
    right.sort()

    for i,j in zip(left,right):
        difs.append(abs(i-j))
    return(sum(difs))

def behandle1b(inputs:list[str])->int:
    left = []
    right = []
    for inn in inputs:
        a,b = (int(i) for i in inn.strip().split())
        left.append(a)
        right.append(b)
    score=0

    for tall in left:
        print(tall * right.count(tall))
        score += tall * right.count(tall)
    
    return score
filnavn = "input.txt"
# filnavn = "ex1.txt"
innlest = lesInput(filnavn)
print(behandle1b(innlest))

