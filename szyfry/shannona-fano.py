
def shannon(array , kod):
    if len(array)>1:
        sum = 0
        sum2=0
        for x, y in array:
            sum += y
            # szukanie polowy sumy prawdopodobienstw
        for x in range(len(array)):
            sum2 += array[x][1]
            if sum2>=sum/2:
                # sa dwie mozliwaosci podzialu albo gdy sum2 jest wieksze od sum albo z gdy sum jest wieksze od sum2
                # wiec nalezy sprawdzic takze mozliwosc o indeks miejsza czy nie ma wtedy miejszej roznicy miedzy polowami
                if abs(sum2-array[x][1]-sum) < abs(sum2-sum):
                    x-=1
                L=array[:x+1]

                for x in range(len(L)):
                    kod[L[x][0]]=kod[L[x][0]]+"0"

                R=array[x+1:]
                for x in range(len(R)):
                    kod[R[x][0]]=kod[R[x][0]]+"1"
                shannon(L, kod)
                shannon(R, kod)
                break



if __name__ == '__main__':
    kod = {"a": "", "b": "", "c": "", "d": "", "e": ""}
    tab = [("a", 0.3), ("b", 0.1), ("c", 0.1), ("d", 0.2), ("e", 0.3)]
    slowo = "baca"

    tab = sorted(tab, key=lambda item: item[1], reverse=True)
    shannon(tab, kod)

    for x in slowo:
        print(kod[x],end=" ")


