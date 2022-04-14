zdanie="szuaknaa dane kot ala ma kota kot ma ale ola niema kota bo nie lubi kotow"
szukane="kot"

def naiwny(zdanie,szukane):
    for x in range(len(zdanie)):
        j=x
        i=0
        while zdanie[j] == szukane[i]:
            if(i+1==len(szukane)):

                print("znaleziono wyraz na pozycji od ",x, " do ",j)
                break
            j+=1
            i+=1
naiwny(zdanie,szukane)