'''Queue Module Implementation'''

class Node:
    '''Node Class Initialization'''
    def __init__(self, value):
        self.value = value
        self.next = None

class queue:
    '''Queue Class Initialization'''
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def isempty(self):
        return self.size == 0


    def enqueue(self, value):
        new_node = Node(value)
        if self.isempty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size +=1
    

    def dequeue(self):
        if not self.isempty():
            removed_item = self.front.value
            self.front = self.front.next
            self.size -= 1
            if self.isempty():
                self.back = None
            return removed_item
        else:
            print("Queue is empty")

class PrintService:
    def __init__(self):
        self.print_queue = queue()

    def submit_document(self, document):
        self.print_queue.enqueue(document)
        print("Document has been submitted successfully: ", document)

    def process_documents(self):
        while not self.print_queue.isempty():
            document = self.print_queue.dequeue()
            print("printing document: ", document)

