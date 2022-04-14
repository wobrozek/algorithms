def enqueue (a):
    global tail
    global head



    if (tail+1==head or (head==0 and tail==len(tablica)-1)):
        print("kolejka jest zapelniona")
    else:
        if len(tablica) - 1 < tail + 1:  # przechodzi na poczatek jesli doszedl do odatniego indexu
            tail = 0
        tablica[tail]=a
        tail+=1                                #dodanie do kolejki


def dequeue ():
    global head
    global tail

    if head!=tail:                #obsluzenie kolejki
        head+=1
        return tablica[head-1]
    else:
        print("kolejka jest pusta")
        return " "


def find(szukana):
    global head
    global tail

    head_kopia=head
    which_in_queue=1
    found=False

    while(head_kopia!=tail):
        if(tablica[head_kopia]==szukana):
            found=True
            print("element ",szukana, "jest ",which_in_queue," w kolejce")
            break
        else:
            head_kopia+=1
            which_in_queue+=1
            if len(tablica) - 1 < head_kopia:  # przechodzi na poczatek jesli doszedl do odatniego indexu
                tail = 0
    if(found==False):
        print("nie znaleziono elementu")



tail=0
head=0
size=10
tablica=[None] *size


enqueue(10)
enqueue(20)
enqueue(490)

find(490)

print(dequeue())
print(dequeue())

enqueue(210)

print(dequeue())
print(dequeue())
print(dequeue())