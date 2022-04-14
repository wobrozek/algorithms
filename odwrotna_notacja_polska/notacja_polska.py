import operator

ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       "^":operator.pow
}

piorytety = {'+': 1,
             '-': 1,
             '*': 2,
             '/': 2,
             ':': 2,
             '^': 3,
             '(': 0}
def onp_to_number(dane, stos):
    for i in dane:
        if i.isnumeric():
            stos.append(float(i))
        else:
            a=float(stos.pop())
            b=float(stos.pop())
            operator=ops[i]

            stos.append(operator(b,a))

def to_onp(dane, stos):
    tab = dane.split()
    output = []

    for i in tab:
        if i.isnumeric():
            output.append(i)
        else:
            if len(stos)==0:
                stos.append(i)
            else:
                if i==')':
                    while len(stos)>0:
                        if stos[-1]=='(':
                            stos.pop()
                            break
                        else:
                            output.append(stos.pop())
                elif piorytety[stos[-1]]<piorytety[i] or i=='(':
                    stos.append(i)
                else:
                    while(True):
                        if len(stos) == 0:
                            stos.append(i)
                            break
                        if piorytety[stos[-1]] < piorytety[i]:
                            stos.append(i)
                            break
                        else:
                            output.append(stos.pop())
    while len(stos) > 0:
        output.append(stos.pop())
    return output


if __name__ == '__main__':
    dane2 = "4 * ( 5 - 6 / 3 + 1 ) ^ 2"
    print(f"dzialanie to {dane2}")
    stos = []
    onp=to_onp(dane2, stos)
    print(f"postac onp to {onp}")
    onp_to_number(onp, stos)
    print(f"wynik dzialania to {stos}")


