import random


def quicsort(array, l ,r):

    if(l<r):
        pivot = random.randint(l, r)
        swap(pivot, r)
        j = l

        for x in range(l, r):
            if (array[x] <= array[r]):
                swap(x, j)
                j += 1
        swap(j, r)
        quicsort(array, l, j - 1)
        quicsort(array, j + 1, r)



def swap(indexa, indexb):           #funkcja zamieniajaca wartosci po podaniu indexow
    global array
    hold=array[indexa]
    array[indexa]=array[indexb]
    array[indexb]=hold



array =[3,20,15,8,25,40,36,72,35,24]
quicsort(array,0,len(array)-1)
print(array)