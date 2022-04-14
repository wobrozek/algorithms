def boyeraMore(zdanie, szukana, tab):
    len_szukana=len(szukana)
    len_zdanie=len(zdanie)
    i=len_szukana-1
    while i<len_zdanie:
        j=len_szukana-1
        while zdanie[i]==szukana[j]:

            if j==0:
                print("znaleziono index na pozycji od: ",i,"do: ",i+len_szukana-1)       #jesli znaleziono przesun tablice o jej dlugosc i wypisz znalezisko
                i+=len_szukana
                j=len_szukana-1
                break
            j-=1
            i-=1

        if zdanie[i]!=szukana[j]:
            i+=len_szukana-(is_tab(zdanie[i])+1)


def is_tab(a):
    global tab
    for x in tab.keys():
        if x==a :
            return tab[x]
    return -1


zdanie = "szuaknaa dane kot ala ma kota kot ma ale ola niema kota bo nie lubi kotow"
szukana = "kot"

tab = {x: index for index, x in enumerate(szukana)}

boyeraMore(zdanie, szukana ,tab)