# Leetcode 206: Reverse Linked List

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
