# leetcode 24 - Swap Nodes in Pairs

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = head
        curr = head.next

        next = head.next.next

        curr.next = prev
        prev.next = self.swapPairs(next)

        return curr
    