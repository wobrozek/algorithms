from heapq import heappop, heappush, heapify

def prim(tab):
    #inicjalizacja tablic
    pred=[]
    k=[]

    for w in range(len(tab)):
        pred.append(0)
        k.append(float('inf'))
    pq=[]
    s=0 #numer wierzcholka drzewa rozpinajacego
    k[s]=0

    for v in range(len(k)):
        heappush(pq ,(float(k[v]), v))
        #pq.put((float(k[v]), v))
    not_visited = []
    for x in range(len(k)):
        not_visited.append(x)


    #algorytm wlasciwy
    while len(pq)>0:
        u=heappop(pq)[1]
        not_visited.remove(u)

        for index, waga in enumerate(tab[u]):
            if waga != 0 and waga != float('inf'):
                if index in not_visited:
                    if waga<k[index]:
                        pred[index] = u
                        k[index] = waga
                        pq[not_visited.index(index)] = (waga, index)
                        heapify(pq)

    for d in range(len(k)):
        print(f"wierzcholek {d+1} laczy sie z wierzcholkiem {pred[d] +1} kosztem {k[d]}")


if __name__=='__main__':
    tab = [[float(x) for x in line.split()] for line in open("C:/Users/wobro/PycharmProjects/prim/input.txt").readlines()]
    prim(tab)

