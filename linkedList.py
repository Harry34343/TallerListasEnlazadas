from Node import Node

class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node
        return
    def Mostrar(self):
        current = self.head
        while current is not None:
            print(str(current.data)+" ->  ", end = "")
            current = current.next
        print("None")
    def DeleteFirst(self):
        if self.head is not None:
            self.head = self.head.next

    def DeleteByValor(self, data):
        current = self.head
        prev = None
        while current is not None:
            if (current.data == data):
                prev.next = current.next
                return
            prev = current
            current = current.next
    def Search(self, data):
        current = self.head
        i=0
        while current.next is not None:
            if (current.data == data):
                return i
            current = current.next
            i=i+1
        return -1
    def Ordenar(self):
        sw = True
        while sw:
            current = self.head
            prev = None
            sw = False
            while current.next is not None:
                next_node = current.next
                if (current.data > next_node.data):
                    current.next = next_node.next
                    next_node.next = current
                    if prev is None:
                        self.head = next_node
                    else:
                        prev.next = next_node
                    sw = True
                    prev = next_node
                else:
                    prev = current
                    current = current.next
    def Invertir(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def size(self):
        i=0
        current = self.head
        while current is not None:
            current = current.next
            i=i+1
        return i

        

