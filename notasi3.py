class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        popped_node = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return popped_node

    def prepend(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, index, nim, nama):
        if index == 0:
            self.prepend(nim, nama)
            return
        new_node = Node(nim, nama)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index out of bounds")
                return
            current = current.next
        if current is None:
            print("Index out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def remove(self, nim):
        current = self.head
        while current:
            if current.nim == nim:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return current
            current = current.next
        print("NIM not found")

    def print_list(self):
        current = self.head
        while current:
            print(f"NIM: {current.nim}, Nama: {current.nama}")
            current = current.next

my_list = DoubleLinkedList()
my_list.append("72", "Mila")
my_list.append("21", "Nabila")
my_list.prepend("10", "Dina")
my_list.insert(1, "87", "Kusuma")
my_list.print_list()

print("\nPop:", my_list.pop().nim)
my_list.print_list()

my_list.remove("21")
print("\nAfter removing NIM 21:")
my_list.print_list()