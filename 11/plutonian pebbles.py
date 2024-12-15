
class Pebble:
    def __init__(self,n):
        self.number:int = int(n) 
        self.next   =   None
        self.prev   =   None
        self.count = 1

    def blink(self):
        # print(self)
        if self.number == 0:
            self.number += 1
            return
        s = str(self.number)

        if self.evenDigits(s):
            a,b = self.splitDigit(s)
            self.number = a
            return Pebble(b)
        
        self.number*=2024

        
    def evenDigits(self,s)->bool:
        # print(self,not len(str(self.number))%2)
        return not len(s)%2  
    
    def splitDigit(self,s)->tuple:
        n=len(s)//2
        a,b = s[:n],s[n:]
        # print(a,b, s)
        return int(a),int(b)
    
    def __str__(self):
        return f"{self.number}"

    def debug(self):
        print(self.prev, self, self.next)

class linkList:
    def __init__(self):
        self.startNode:Pebble = None
        self.lastNode:Pebble = None
        self.sett = []
        self.iterasjon = 0

    def remove(self, this:Pebble):
        if this == self.startNode:
            self.startNode = this.next
            this.next.prev = None
            return
        if this == self.lastNode:
            self.lastNode = this.prev
            this.prev.next = None
            return
        # print(this.debug())
        this.prev.next  =   this.next
        this.next.prev  =   this.prev
    
    def pop(self,indeks:int):
        curr= self.startNode
        while indeks:
            indeks -= 1
            curr = curr.next
        self.remove(curr)
        return curr

    # a |b| c 

    def append(self,this:Pebble):
        # Om det er første node:
        if self.startNode == None:
            self.startNode = this
            self.lastNode = this
            return self
        
        self.lastNode.next = this
        this.prev = self.lastNode
        self.lastNode = this

    def __str__(self):
        s=""
        curr = self.startNode
        
        while curr != None:
            curr.debug()
            s += f"{curr} "
            curr = curr.next
        return s

    def iter(self):
        curr = self.startNode
        while curr != None:
            res = curr.blink()
            next = curr.next  
            if res:
                # Må legge til en ny stein
                curr.next = res
                res.prev = curr
                res.next = next
                if next:
                    next.prev = res
                else:
                    self.lastNode=res
            curr = next

    def __len__(self):
        i = 0
        unike=[]
        curr:Pebble = self.startNode
        while curr != None:
            i+=1
            if curr.number not in self.sett:
                self.sett.append(curr.number)
            if curr.number not in unike:
                unike.append(curr.number)
            
            curr = curr.next
        # print("Sett unike ",len(self.sett))
        # print("Nåvæ unike ",len(unike))
        return i



filnavn = "eks1.txt"
filnavn = "input.txt"
pebbles:list[Pebble] = []
links = linkList()
with open(filnavn) as fil:
    for s in fil.readline().split():
        pebbles.append(Pebble(s))
        links.append(Pebble(s))
links = linkList()
links.append(Pebble(0))
def visPebbles():
    for i in pebbles:
        print(i,end=" ")
    print()
# visPebbles()
nye_steiner =[]
# print(links)
## Må fikse logikken for nye steiner

for _ in range(4):
    print(f"After {_+1} blinks:")
    links.iter()
    print(links)
    # print(len(links))
    
links.pop(2) #Popping fungerer
print(links)
# print(len(links))

# Hva er viktig: Antall steiner, ikke nødvendigvis antall steiner
# Så 1. forbedring: Summere lignende tall. Så kun unike stein-antall