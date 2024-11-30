# Tree traversal refers to the process of visiting each node in a tree data structure, 
# covering all the nodes in a specific order.  

# Breadth-first search. (BFS)
#Breadth-First search explores a tree level by level, 
#starting from the root and moving horizontally across the levels.

# Depth-First search. (DFS)
# Depth-First search explores a tree by going as deep as possible along one branch before backtracking.

# Types of DFS
#1. In-order
#2. Pre-order
#3. Post-order


# Tree traversal: In-order
# In-order traversal is a tree traversal algorithm that recursively performs an in-order traversal 
# on the left subtree, visits the root node, and finally performs an in-order traversal 
# on the right sub-tree. 

# left child -> root node -> right node

def in_order_traversal(node):
    '''In-order traversal'''
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end = " ")
        in_order_traversal(node.right)

# Tree traversal: Pre-order
# Pre-order traversal is a tree traversal that visits the root node first, 
# then recursively performs a pre-order traversal on the left subtree, 
# and finally on the right subtree.

# root node -> left child -> right child.

def pre_order_traversal(node):
    '''Pre-order traversal'''
    if node is not None:
        print(node.value, end = " ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Tree traversal: Post-order
# Post-order traversal is a tree traversal algorithm that recursively performs a post-order
# traversal on the left subtree, then on the right subtree, and finally visits the root node.

# left child -> right child -> root node

def post_order_traversal(node):
    '''Post-order traversal'''
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end = " ")

