''' Binary Search Tree Implementation'''

class Node:
    '''Node class implementation'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    '''Binary search tree implementation'''
    def __init__(self):
        self.root = None

    def insert(self, value):
        '''Insert method'''
        if not self.root:
            self.root = Node(value)
            return

        temp = self.root
        while temp:
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                return
    
    def search (self, value):
        '''search method implementation'''
        temp = self.root
        while temp:
            if value == temp.value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None


            
            
