
class Element:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Lista:
    def __init__(self):
        self.head=None
        self.tail=None

    def show(self):
        current=self.head
        while(current!=self.tail):
            print(current.data)
            current=current.next
        print(self.tail.data)

    def push(self,data=0,index=None):
        if(self.head==None):
            self.head=Element(data)
            self.tail=Element(None)
            self.head.prev=self.tail
            self.head.next=self.tail
            self.tail.next=self.head
            self.tail.prev=self.head
        else:
            if(self.tail.data==None):
                self.tail.data=data
            else: 
                if(index==None):                                #funkcja bez indexu dodaje na końcu          
                    nowy=Element(data)
                    nowy.next=self.tail.next
                    nowy.prev=self.tail
                    self.tail.next=nowy  
                    self.tail=nowy
                else:
                    current=self.head
                    for x in range(index):                      #przechodzi do podanego elementu
                        if(current==None):
                            print("podany index jest poza obecnym rozmiarem listy mozesz uzyc funkcji bez tego parametru by doodac cos na koniec listy")
                            break
                        else:
                            current=current.next
                    if(current!=None):                          #jesli dany index jest w srodku listy to element zanim wpisz jako element nastepny po dodanym
                        kopia_data=current.data
                        kopia_next=current.next
                        current.data=data
                        current.next=Element(kopia_data)
                        current.next.next=kopia_next
                        current.next.prev=current
                        current.next.next.prev=current.next.next

    def push_in_front(self,data):
        if(self.head==None):
            self.head=Element(data)
        else:
            nowy=Element(data)
            nowy.prev=self.head.prev
            nowy.next=self.head 
            self.head.prev=nowy
            self.head=nowy


    def delete(self,index):
        current=self.head

        for x in range(index-2):
            if(current.next==None):
                print("podany index jest poza obecnym rozmiarem listy")
                break
            else:
                current=current.next
        if(current.next!=None):
            current.next=current.next.next
            current.next.next.prev=current

    def find(self,szukana):
        current=self.head
        a=0
        while(current!=self.tail):
            if(szukana==current.data):
                print("znaleziono podana wartosc na indexie ",a)
                return
            current=current.next
            a+=1
        if(szukana==self.tail.data):
                print("znaleziono podana wartosc na indexie ",a)
                return
        print("nie znaleziono szukanej warosci")
        


nowa_lista=Lista()
nowa_lista.push(1)
nowa_lista.push(2)
nowa_lista.push(3)
nowa_lista.push(4)
nowa_lista.delete(2)
nowa_lista.push(6)
nowa_lista.push_in_front(5)

nowa_lista.show()
nowa_lista.find(5)