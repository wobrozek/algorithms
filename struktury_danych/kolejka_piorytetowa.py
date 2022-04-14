def enqueue(a, prio):
    global tail
    global head

    if (tail + 1 == head or (head == 0 and tail == len(tablica) - 1)):
        print("kolejka jest zapelniona")
    else:
        if len(tablica) - 1 < tail + 1:  # przechodzi na poczatek jesli doszedl do odatniego indexu
            tail = 0

        head_kopia = head
        miejsce_dodania=tail
        while (head_kopia - tail != 0):
            if (prio < tablica[head_kopia][1]):  # jesli znajdzie element o gorszym(wiekszym) piorytecie
                miejsce_dodania=head_kopia
                tablica_kopie = [None] * size
                for x in range(size):
                    tablica_kopie[x] = [None] * 2
                while (head_kopia - tail != 0):         # przenosi tablice o jeden w momecie znalezienia miejsca do dodania
                    tablica_kopie[head_kopia][0]=tablica[head_kopia+1][0]
                    tablica_kopie[head_kopia][1]=tablica[head_kopia+1][1]

                    if(miejsce_dodania==head_kopia):            #jelis to pierwszy element przenies w przeciwnym razie odwolaj sie do kopi
                        tablica[head_kopia+1][0]=tablica[head_kopia][0]
                        tablica[head_kopia+1][1]=tablica[head_kopia][1]
                    else:
                        tablica[head_kopia+1][0]=tablica_kopie[head_kopia-1][0]
                        tablica[head_kopia+1][1]=tablica_kopie[head_kopia-1][1]
                    head_kopia += 1

            if (head_kopia - tail != 0):
                head_kopia += 1

        tablica[miejsce_dodania][1] = prio
        tablica[miejsce_dodania][0] = a
        tail += 1  # dodanie do kolejki


def find(szukana):
    global head
    global tail

    head_kopia=head
    which_in_queue=1
    found=False

    while(head_kopia!=tail):
        if(tablica[head_kopia][0]==szukana):
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




def dequeue():
    global head
    global tail

    if head != tail:  # obsluzenie kolejki
        head += 1
        return tablica[head - 1][0]
    else:
        print("kolejka jest pusta")
        return " "


tail = 0
head = 0
size = 10

tablica = [None] * size

for x in range(size):
    tablica[x] = [None] * 2  # deklarowanie tablicy dwuelementowej

enqueue(10, 3)
enqueue(20, 2)
enqueue(490, 2)
enqueue(8, 1) #ma piorytet najmniejszy wiec zostanie dodany pierwszy

find(20)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())