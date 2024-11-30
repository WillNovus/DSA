'''Trie Class Implementation'''

class TrieNode:
    '''TrieNode Initialization'''
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    '''Trie implementation'''
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        '''TrieNode insert function'''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        '''TrieNode search function'''
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def delete(self, word):
        '''TrieNode Delete Function'''
        node = self.root
        stack = [] # Stack to track the path
        for char in word:
            if char not in node.children:
                return # Word doesn't exist
            stack.append((node, char))    
            node = node.children[char]

        if not node.is_word:
            return #Word doesn't exist
        
        # Un-mark the last node's 'is_word' flag
        node.is_word = False

        # Now clean up the nodes from the stack (if needed)
        while stack:
            parent, char = stack.pop() 

            # Check if the current word has any children or is marked as another word.
            if not node.children and not node.is_word:
                # if no children and it's not the end of another word, remove the child node
                del parent.children[char]
            else:
                #stop the cleanup as soon as we find a node that can't be deleted.
                break
                #Move back to the parent node for the next iteration.
        node = parent


            
