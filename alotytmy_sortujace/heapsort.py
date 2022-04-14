def heapsort(array):
    n=len(array)-1
    #petla tworzaca posortowany kopiec
    for i in range(int(n/2),0,-1):
        heapify(array,i,n)
    #petla usuwajaca element zgory
    while n>=2:
        swap(n,1)
        n-=1
        heapify(array,1,n)

def heapify(array,i,m):
    l=i*2
    p=i*2+1
    max=i

    if l <= m and array[l]>array[max]:
        max=l

    if p <= m and array[p] > array[max]:
        max=p

    if max!=i:
        swap(i,max)
        heapify(array,max,m)

def swap(indexa, indexb):           #funkcja zamieniajaca wartosci po podaniu indexow
    global array
    hold=array[indexa]
    array[indexa]=array[indexb]
    array[indexb]=hold



array =[3,20,15,8,25,40,36,72,35,24]
heapsort(array)
print(array)