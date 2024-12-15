filnavn = "eks1.txt"
filnavn = "input.txt"

with open(filnavn) as fil:
    linje = fil.readline().strip()
print(linje)

disk = []
fil = False
indeks = -1
empty = {
                    "ID":-1,
                    "rep":"."
                }
for tall in linje:
    fil = not fil
    if fil:
        indeks+=1
        for _ in range(int(tall)):
            disk.append(
                {
                    "ID":indeks,
                    "rep":str(indeks)[0]
                }
            )
            
    else:
        for _ in range(int(tall)):
            disk.append(
                empty
            )


def visDisk(liste):
    for info in liste:
        print(info["rep"],end="")
    print()

visDisk(disk)

# flytt filer
i = 0
j = len(disk)-1
while i <= j:

    if disk[i]["ID"]!=-1:
        i += 1
    elif disk[j]["ID"]!=-1:
        # om i er tom og j ikke er det: 
        disk[i] = disk[j]
        disk[j] = empty
        i += 1
    else:
        j-=1

visDisk(disk)
løsning = 0 
for i in range(len(disk)):
    if disk[i]["ID"]!= -1:
        løsning+= i * disk[i]["ID"]
print(løsning)