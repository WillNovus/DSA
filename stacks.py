'''Class implementation of Stack'''

class Node:
    '''Node Initialization'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    '''Stack Initialization'''
    def __init__(self):
        self.top = None

    def push(self, value):
        '''Stack push method'''
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        '''Stack pop method'''
        if not self.is_empty():
            popped_item = self.top.value
            self.top = self.top.next
            return popped_item
        
    def is_empty(self):
        '''Stack empty method'''
        return self.top is None

class TextEditor:
    '''Text Editor Application'''
    def __init__(self):
        self.content = " "
        self.undo_stack =  Stack()
    
    def add_text(self, text):
        '''Add text method'''
        self.content += text
        self.undo_stack.push(len(text))

    def undo(self):
        '''Undo text method'''
        if not self.undo_stack.is_empty():
            length = self.undo_stack.pop()
            self.content = self.content[:-length]

    def display(self):
        '''Display text method'''
        print("Displaying Content:  ")
        print(self.content)

Editor = TextEditor()

Editor.add_text("Hello ")
Editor.add_text("Will!")

Editor.display()

Editor.undo()

Editor.display()

#End of File