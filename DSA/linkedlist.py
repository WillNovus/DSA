'''LinkedList Class Module'''

class Node:
    '''LinkedList Node Class Initialization'''
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    '''LinkedList class Initialization'''
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        '''Append Method'''
        #Appending a node has a constant time complexity.
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        '''Prepend Method'''
        #Prepending a node has a constant time complexity.
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def iterate(self):
        '''Iterate Method'''
        iterator = self.head
        while iterator:
            print (iterator.value + " ")
            iterator = iterator.next

    def remove(self, value):
        '''Remove method'''
        #Removing the first node has a constant time complexity.
        #Traversing the linked list has a linear time complexity o(n).
        #removing a node other than the first has a linear time complexity.
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
                return
        iterator = self.head

        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                    return
            iterator = iterator.next

class ShoppingCart:
    '''Shopping Cart Class'''
    def __init__(self):
        self.items = LinkedList()

    def add_item(self, item):
        '''Method to add items'''
        self.items.append(item)

    def remove_item(self, item):
        '''Method to remove items'''
        self.items.remove(item)

    def display_cart(self):
        '''Method to display cart items.'''
        print("Items in the shopping cart: ")
        self.items.iterate()

cart = ShoppingCart()

cart.add_item("Oranges")
cart.add_item("Apples")
cart.add_item("Grapes")

cart.display_cart()

cart.remove_item("Oranges")

cart.display_cart()