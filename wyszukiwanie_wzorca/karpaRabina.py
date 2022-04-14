import math


def karpaRabina(zdanie, szukana , tab):

    lenSzukana=len(szukana)
    lenTab=len(tab)
    zdanieHash=0
    szukanaHash=0
    # pierwsze haszowanie
    x=0
    while x<lenSzukana:
        zdanieHash+=(math.pow(lenTab,lenSzukana-1-x)*tab[zdanie[x]])
        szukanaHash+=(math.pow(lenTab,lenSzukana-1-x)*tab[szukana[x]])
        x+=1
    zdanieHash %=1483
    szukanaHash %=1483
    #haszowanie dla każdej kolejnej litery
    while x<len(zdanie):
        if zdanieHash==szukanaHash:
            print("znaleziono index na pozycji od: ", x - lenSzukana , "do: ",x-1 )
        wartoscUsuwana=math.pow(lenTab,lenSzukana-1) * (tab[zdanie[x-lenSzukana]])
        wartoscDodawana=tab[zdanie[x]]
        zdanieHash=((zdanieHash-wartoscUsuwana) * lenTab+wartoscDodawana) % 1483
        x+=1




zdanie = "szuaknaa dane kot ala ma kota kot ma ale ola niema kota bo nie lubi kotow"
szukana = "kot"
tab={}
y=0
for z,x in enumerate(zdanie):
    if x not in tab.keys() :
        tab[x]=y
        y+=1

karpaRabina(zdanie, szukana ,tab)