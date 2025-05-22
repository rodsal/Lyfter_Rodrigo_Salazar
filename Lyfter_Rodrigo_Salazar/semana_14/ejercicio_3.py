"""
3. Cree una estructura de objetos que asemeje un Binary Tree.
    1. Debe incluir un método para hacer `print` de toda la estructura.
    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def has_right (self):
        return self.right != None
    
    def has_left (self):
        return self.left != None

    def pre_order (self):
        print(self.data)
        if self.has_left():
            self.left.pre_order()
        if self.has_right():
            self.right.pre_order()
    
    def in_order (self):
        if self.has_left():
            self.left.in_order()
        print(self.data)
        if self.has_right():
            self.right.in_order()

    def post_order (self):
        if self.has_left():
            self.left.post_order()
        if self.has_right():
            self.right.post_order()
        print(self.data)

    def insert(self, new_node):
        if self.data == new_node.data:
            raise ValueError("El elemento ya esta en el arbol")
        elif new_node.data < self.data:
            if self.has_left():
                self.left.insert(new_node)
            else:
                self.left = new_node
        else:
            if self.has_right():
                self.right.insert(new_node)
            else:
                self.right = new_node



class BinaryTree:
    def __init__(self):
        self.root = None
    
    def print_structure(self):
        def print_tree(node, level=0):
            if node is not None:
                print_tree(node.right, level + 1)
                print("     " * level + str(node.data))
                print_tree(node.left, level + 1)
        if self.root is None:
            raise IndexError ("Arbol Vacío.")
        else:
            print_tree(self.root)
    
    def is_empty(self):
        return self.root == None
    
    def pre_order(self):
        if not self.is_empty():
            self.root.pre_order()
        else:
            raise IndexError("Arbol vacio.")
    
    def in_order(self):
        if not self.is_empty():
            self.root.pre_order()
        else:
            raise IndexError("Arbol vacio.")

    def post_order(self):
        if not self.is_empty():
            self.root.pre_order()
        else:
            raise IndexError("Arbol vacio.")
    
    def insert (self, new_node):
        if self.is_empty():
            self.root = new_node
        else:
            self.root.insert(new_node)


arbol_1 = BinaryTree()
first_node = Node(35)
arbol_1.insert(first_node)
second_node = Node(76)
arbol_1.insert(second_node)
third_node = Node(15)
arbol_1.insert(third_node)
forth_node = Node(10)
arbol_1.insert(forth_node)
fifth_node = Node(80)
arbol_1.insert(fifth_node)
sixth_node = Node(45)
arbol_1.insert(sixth_node)
arbol_1.print_structure()





