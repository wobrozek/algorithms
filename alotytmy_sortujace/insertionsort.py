def insertionsort(array):
    for x in range(1,len(array)):
        for y in range(0,x-1):
            if array[x]<array[y]:
                hold=array[x]
                array[x]=array[y]
                array[y]=hold


array =[3,20,15,8,25,40,36,72,35,24]
insertionsort(array)
print(array)