def cezar(tekst):
    key=6
    for x in tekst:
        if x!=' ':
            zaszyfrowane = ord(x) + key

            if zaszyfrowane > 122:
                zaszyfrowane -= 26

            print(chr(zaszyfrowane), end="")
        else:
            print(" ",end="")



if __name__ == '__main__':
    tekst = "algorytmy kodowania tekst do zakodowania "
    print("orginal: ")
    print(tekst)
    print("tekst zaszyfrowany: ")

    cezar(tekst)

