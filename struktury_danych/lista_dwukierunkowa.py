class Element:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Lista:
    def __init__(self):
        self.head=None

    def show(self):
        current=self.head
        while(current!=None):
            print(current.data)
            current=current.next


    def push(self,data=0,index=None):
        if(self.head==None):
            self.head=Element(data)
        else:
            current=self.head   
            if(index==None):                                #funkcja bez indexu dodaje na końcu             
                while(current.next!=None):
                    current=current.next
                current.next=Element(data)
                current.next.prev=current
            else:
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
            self.head.prev=nowy
            nowy.next=self.head 
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
        while(current!=None):
            if(szukana==current.data):
                print("znaleziono podana wartosc na indexie ",a)
                return
            current=current.next
            a+=1
        print("nie znaleziono szukanej warosci")



nowa_lista=Lista()
nowa_lista.push(1)
nowa_lista.push_in_front(2)
nowa_lista.push(3)
nowa_lista.push(4)
nowa_lista.push(5)
nowa_lista.push(6)
nowa_lista.show()