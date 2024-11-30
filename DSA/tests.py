
#Middle of a linked list.
# Given a non-empty, singly linked list with node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
from linkedlist import LinkedList, Node


class list(LinkedList):
    def __init__(self):
        super().__init__()

    def middle_node(self, head:Node):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            return slow
        
    def loop_detect(self, head:Node):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                print("Loop Found")
                return True
        print("Loop not Found")
        return False

    def reverse(self):
        reverse = None
        current = self.head
        while current:
            forward = current.next
            current.next = reverse
            reverse = current
            current = forward
            return reverse

    def RemoveDuplicate(self):
        DeleteMe = self.Node()
        curr = self.head
        while curr.head!= None:
            if curr.head != None and curr.value == curr.next.value:
                DeleteMe = curr.head
                curr.head.next = DeleteMe.next
                if DeleteMe == self.tail:
                    self.tail = curr
            else:
                curr = curr.next

