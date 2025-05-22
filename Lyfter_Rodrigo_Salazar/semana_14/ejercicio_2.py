"""
2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleEndedQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def print_structure(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("")

    def push_right(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    
    def push_left(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
    def pop_left(self):
        if self.head:
            if self.head == self.tail:
                self.tail = None
                self.head = self.tail
            else:
                self.head = self.head.next
                self.head.previous = None

        
    
    def pop_right(self):
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = self.head
            else:
                self.tail = self.tail.previous
                self.tail.next = None


first_node = Node("Hola")
my_dequeue = DoubleEndedQueue()
my_dequeue.push_left(first_node)
# my_queue.print_structure()

second_node = Node("Mundo")
my_dequeue.push_right(second_node)

third_node = Node("third")
my_dequeue.push_left(third_node)

my_dequeue.print_structure()

print("Quita en la izquierda")
my_dequeue.pop_left()
my_dequeue.print_structure()

print("Quita en la derecha")
my_dequeue.pop_right()
my_dequeue.print_structure()
