# Leetcode 203. Remove Linked List Elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        curr = dummy

        while curr.next:
            if curr.next.val == val：
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next