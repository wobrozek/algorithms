
def huffman(tab, slowo ,kod):
    tab = sorted(tab, key=lambda item: item[1], reverse=True)
    while len(tab)>=2:

        min1 = tab.pop()
        min2 = tab.pop()

        for x in min1[0]:
            kod[x]="0" +kod[x]

        for x in min2[0]:
            kod[x]="1" +kod[x]

        sum = (min1[0] + min2[0], min1[1] + min2[1])
        tab.append(sum)
        tab = sorted(tab, key=lambda item: item[1], reverse=True)




if __name__ == '__main__':
    kod = {"a":"", "b":"", "c":"", "d":"", "e":"", "f":""}
    tab = [("a", 0.3), ("b", 0.1), ("c", 0.2), ("d", 0.1), ("e", 0.2), ("f", 0.1)]
    slowo="baca"
    huffman(tab,slowo,kod)

    for x in slowo:
        for y in range(len(kod[x])-1,-1,-1 ):   # wypisanie kodu od tylu
            print(kod[x][y],end="")
        print(" ",end="")

