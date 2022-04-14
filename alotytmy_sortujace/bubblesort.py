def bubblesort(array):
    for y in range(len(array), 0, -1):
        for x in range(0, y-1):
            if array[x]>array[x+1]:
               hold=array[x+1]
               array[x+1]=array[x]
               array[x]=hold


array =[3,20,15,8,25,40,36,72,35,24]
bubblesort(array)
print(array)