from heapq import heappop, heappush, heapify

def dijkstry(tab):
    #inicjalizacja tablic
    pred=[]
    dist=[]
    q=[]
    qs = []

    for w in range(len(tab)):
        pred.append(0)
        dist.append(float('inf'))
        heappush(q, (float(dist[w]), w))
        qs.append(w)

    s=0 #numer wierzcholka drzewa rozpinajacego
    dist[s]=0

    #algorytm wlasciwy
    while len(q)>0:
        u = heappop(q)[1]
        qs.remove(u)

        for index, waga in enumerate(tab[u]):
            if waga != 0.0 and waga != float('inf'):
                d=dist[u] + tab[u][index]
                if d < dist[index]:
                    dist[index]= d
                    pred[index] = u
    print(f"{pred} tablica zanizona o jeden przez posaidanie indeksu zero")
    print(dist)
    print(f"najkrotsza droga z punktu 1 do punktu 5 jest przez punkty:",end=" ")
    cel=5-1

    while cel !=0:
        cel=pred[cel]
        if cel !=0:
            print(cel + 1, end=" ")

    print(f"i wynosi {dist[5-1]}")




if __name__ == '__main__':
    tab = [[float(x) for x in line.split()] for line in
           open("input.txt").readlines()]
    dijkstry(tab)


