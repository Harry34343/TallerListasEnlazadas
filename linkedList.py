import Node

class linkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node.Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node.Node(data)

        if (self.head is None):
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return
    
    def recorrer(self):
        current = self.head
        while current is not None:
            print(str(current.data) + " -> ", end="")
            current = current.next
        print("None")

    def search(self, data):
        i=0
        current = self.head
        while current is not None:
            if current.data == data:
                return i
            i=i+1
            current = current.next
        return -1

    def ordenar(self):
        intercambio = True
        while intercambio:
            intercambio = False
            current = self.head
            prev = None
            while current.next:
                next_node = current.next
                if current.data > next_node.data:
                    current.next = next_node.next
                    next_node.next = current
                    if not prev:
                        self.head = next_node
                    else:
                        prev.next = next_node
                    prev = next_node
                    intercambio = True
                else:
                    prev = current
                    current = current.next



    def invertir(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
            
    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next 

    def delete_by_value(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                current = current.next
                return
            current = current.next
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
