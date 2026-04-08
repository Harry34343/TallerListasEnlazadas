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
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if current.data > next_node.data:
                    temp = current.data
                    next_node.data = temp
                    current.data = next_node.data
                next_node = next_node.next
            current = current.next

    def recorrerOrdenado(self):
        newLinkedList = linkedList()
        newLinkedList.head = self.head
        newLinkedList.ordenar()
        newLinkedList.recorrer()
