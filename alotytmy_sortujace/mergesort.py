


def mergeSort(array):
    if len(array) > 1:
        srednia = int(len(array)/2)
        l = array[:srednia]
        r = array[srednia:]
        mergeSort(l)
        mergeSort(r)
        merge(array,l,r)


def merge(array,l,r):
    head1 = head2 = k = 0
    while head1 < len(l) and head2 < len(r):
        if l[head1]<r[head2]:
            array[k]=l[head1]
            head1+=1
        else:
            array[k]=r[head2]
            head2+=1
        k+=1

        # dodanie elementow najweikszych ktore nie zostaly dodane przez porownanie
    while head1 < len(l):
        array[k] = l[head1]
        head1 += 1
        k += 1

    while head2 < len(r):
        array[k] = r[head2]
        head2 += 1
        k += 1



array =[3,20,15,8,25,40,36,72,35,24]
mergeSort(array)
print(array)