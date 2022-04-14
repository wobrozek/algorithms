def push (a):
    global top

    if top==len(tablica)-1:
        print("stos jest pelny")
    else:
        tablica[top]=a
        top+=1

                             #dodanie do stosu


def pop ():
    global top

    if top>0:
        top-=1
        print("usunieto ze stosu ",tablica[top])
        return tablica[top]
    else:
        print("stos jest pusty")

                    #usuniecie ze stosu

def find(szukana):
    global top

    a=top-1
    found=False
    elements_to_dequeue=0

    while(a>=0):
        if(tablica[a]==szukana):
            print("by dostac sie do ",szukana, "musisz sciagnac ",elements_to_dequeue," elementow ze stosu")
            found=True
            break
        a-=1
        elements_to_dequeue+=1
    if(found==False):
        print("elementu nie ma w stosie")

top=0
size=10
tablica=[None] *size

pop()
push(10)
push(20)

find(20)
find(400)

pop()

push(12)
pop()

