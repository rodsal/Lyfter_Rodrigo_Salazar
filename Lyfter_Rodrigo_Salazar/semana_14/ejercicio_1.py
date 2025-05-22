"""
1. Cree una estructura de objetos que asemeje un Stack.
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
    """

class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self):
        self.top = None

    def print_structure(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            self.top = self.top.next


first_node = Node(6)
my_stack = Stack()
my_stack.push(first_node)
# my_queue.print_structure()

second_node = Node(9)
my_stack.push(second_node)

third_node = Node(7)
my_stack.push(third_node)

forth = Node(4)
my_stack.push(forth)

my_stack.print_structure()

print("Pop")

my_stack.pop()
my_stack.print_structure()










