if __name__=='__main__':
    dane = "7;5.4;3;8;3;6;218;6.4;"
    i = 0
    tab = []
    poczatek_cyfry=0

    while i < len(dane):
        if dane[i] == ';':
            tab.append(float(dane[poczatek_cyfry:i]))
            poczatek_cyfry = i+1
        i += 1
    print(f"dane: {dane}")
    for x in tab:
        print(x)

    max=tab[0]
    for x in tab:
        if x>max:
            max=x

    print(f'maksymalna wartość to {max}')




