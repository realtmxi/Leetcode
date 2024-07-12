# Leetcoce 19. Remove Nth Node From End of List
from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[Node], n: int) -> Node:
        dummy = Node(0, head)

        slow = fast = dummy

        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next