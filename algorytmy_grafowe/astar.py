from heapq import heappop, heappush, heapify

def dijkstry(tab):
    #inicjalizacja tablic
    pred=[]
    dist=[]
    q=[]
    qs = []

    s=[]
    h=[4 ,8,3,4,5,2,1,0]

    for w in range(len(tab)):
        pred.append(0)
        dist.append(float('inf'))
        heappush(q, (float(dist[w]), w))

    start=0
    cel=7
    droga=0

    #algorytm wlasciwy
    while len(q)>0:
        u = heappop(q)[1]
        qs.append(u)
        s.append(u)

        for index, waga in enumerate(tab[u]):
            if waga != 0.0 and waga != float('inf'):
                if not index in qs:
                    if not index in s:
                        heappush(q, (droga+waga+h[index], index))
                        qs.append(index)
                        pred[index] = u
        if u==cel: break


    print(f"{pred} tablica zanizona o jeden przez posaidanie indeksu zero")
    print(s)
    print(f"najkrotsza droga z punktu 1 do punktu 8 jest przez punkty:",end=" ")
    cel=8-1

    while cel !=0:
        cel=pred[cel]
        if cel !=0:
            print(cel + 1, end=" ")

    print(f"i wynosi {pred[8-1]}")




if __name__ == '__main__':
    tab = [[float(x) for x in line.split()] for line in
           open("inputastar.txt").readlines()]
    dijkstry(tab)


