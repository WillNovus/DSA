
import heapq 

#Reverse a singly linked list. 
class Node:
    '''Linked List Node '''
    def __init__(self, value):
        self.next = None
        self.value = value

class Solution:
    '''Reversed List Solution'''
    def reversed_list(self, head: Node):
        '''Reversed List Solution'''
        reverse = None
        while head:
            forward = head.next
            head.next = reverse
            reverse = head
            head = forward
        return reverse

#Middle of a linked list.
# Given a non-empty, singly linked list with node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

class Solution2:
    '''Solution to the middle of a linked list'''
    def middle_node(self, head: Node):
        '''middle of a linked list using the tortoise and hare algo'''
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


#Reverse string using a stack 
#Write a function that takes a string as input and returns the string using a stack
class Solution3:
    '''Reverse a string'''
    def reverse(self, input_str):
        ''' Reverse a string.'''
        stack = []
        for char in input_str:
            stack.append(char)
        reverse = " "
        while stack:
            reverse += stack.pop()
        return reverse
    
class SOlution3b:
    '''Reverse a string'''
    def reverse(self, str):
        return str[::-1]

class Solution4:
    '''Necessary doc string'''

    #Valid Parentheses
    #Given the string s containing just the characters '(', ')', '{', '}', '[' and ']'
    #determine if the input string is valid.
    #An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close brackets has a corresponding open bracket of the same type.

    def is_valid(self, s):
        '''valid parentheses call'''
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or (c == ')' and stack[-1] != '(') \
                or (c == ']' and stack[-1] != '[') \
                or (c == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack
    
class SOlution4b:
    def isValid(self, s):
        """
        :type s: str
        :rt: bool
        """
        stack = []
        match = {'(':')', '[':']', '{':'}'}
        
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False
        return not stack
                

#Solution5
    # Implement queue using Sacks. 
    # Implement a first in first out FIFO queue using only two stacks. 
    # The implemented queue should support all the functions of a normal queue. (push, peek, pop and empty.)

class MyQueue:
    '''Queue Implementation'''

    def __init__(self):
        self.stack = []
        self.reversed = []
        self.top = None

    def push(self, x:int) -> None:
        '''Queue push method'''
        self.stack.append(x)

    def pop(self) -> int:
        '''Queue pop method'''
        self.peek()
        return self.reversed.pop()

    def peek(self) -> int:
        '''Queue push method'''
        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed[-1]

    def empty(self) -> bool:
        '''Queue empty method'''
        return not self.stack and not self.reversed
    
#Remove Duplicates
# Implement a function that takes an input array, removes the duplicate elements and return the results of the array.

def remove_duplicates(input_array):
    '''Removes duplicates in an array'''
    unique_elements = list(set(input_array))
    return unique_elements


# Search in a Binary search tree. Given the root of a binary search tree and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. if such a node does not exist, return null.

def search_bst(root, val):
    ''' Binary Search Tree'''
    if not root:
        return None
    if root.val == val:
        return root
    if val > root.val:
        return search_bst(root.right, val)
    return search_bst(root.left, val) 

#Alternatively 

def search_bst_alt(root, val):
    '''Alternative Search BST method'''
    while root:
        if root.val == root:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
        return root
# Design a class to find the Kth largest element in a stream.
# Note that it is the kth largest element in a sorted order, not the kth distinct element.  

class KthLargest:
    ''' Kth Largest Element in a Stream'''

    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val:int) -> int:
        ''' To add values to the heap '''
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Given an array of integers, return indies of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.

def two_sum(nums, target):
    ''' twoSum leet-code problem'''
    num_to_index = {}

    for num, i in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        
        num_to_index[num] = i
    
    return []

# Alternative Solution

class Solution5:
    ''' Two Sum Challenge'''
    def two_sum(self, nums:list[int], target:int):
        '''two sum doc string'''
        num_dict = {}
        n = len(nums)

        for i in range(n):
            num_dict[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in num_dict and num_dict[complement] != i:
                return [num_dict[complement], i]

        return [] 


#Leet-code Challenge - Count Pairs Whose Sum is Less than Target
#Given a 0-indexed integer array nums of length n and an integer target, 
#return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target

def count_pairs(nums, target):
    '''Count the pairs whose sum is less than the target.'''
    pairs = 0
    nums.sort()
    p1, p2 = 0, len(nums)-1

    while p1 < p2:
        if nums[p1] + nums[p2] < target:
            pairs += p2 - p1
            p1 += 1
        else:
            p2 -= 1
    return pairs


# Implement the factorial function using recursion.
#Factorial Function (factorial):
#Calculates the factorial of a non-negative integer n using recursion.
#The factorial of n is the product of all positive integers less than or equal to n.

def factorial(n):
    '''Factorial example'''
    # Implement this function
    if n <= 1:
        return 1
    return n * factorial(n-1)


# Leet-code Challenge - Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
# That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# My Solution
def fib(n):
    '''Any variable will do.'''
    # The fibonacci number.
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

#An alternative efficient solution
class Solution6(object):
    '''This includes memoization.'''
    memo = {}
    def fib(self, n):
        '''The fibonacci.'''
        if n == 0 or n == 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n - 1) or self.fib(n - 2)
        return self.memo[n]


# Leet-code Challenge - Range Sum of BST
# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

def range_sum_bst(root, low, high):
    ''' Range Sum of Binary Search Tree'''
    # Write your code here
    def helper(node):
        if not node:
            return 0
        if node.val > high:
            return helper(node.left)
        if node.val < low:
            return helper(node.right)
            
        return node.val + helper(node.left) + helper(node.right)
    return helper(root)    

# Alternative method

class TreeNode(object):
    '''TreeNode Class Implementation'''
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    
    def range_sum_bst(self, root, high, low):
        '''Range Sum of Binary Search Tree'''
        if root is None:
            return 0
        if root.val > high:
            return range_sum_bst(root.left, low, high)
        elif root.val < low:
            return range_sum_bst(root.right, low, high)
        
        result = root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

        return result