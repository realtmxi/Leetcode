from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next1 = l1.next
        next2 = l2.next
        if l1.val + l2.val < 10:
            lst = ListNode(l1.val+l2.val, None)
            curr = lst
            lead = 0
        else:
            lst = ListNode(l1.val+l2.val-10, None)
            curr = lst
            lead = 1
        while (next1 != None or next2 != None or lead != 0):
            if next1 != None and next2 != None:
                if next1.val + next2.val + lead < 10:
                    temp = ListNode(next1.val+next2.val + lead, None)
                    lead = 0
                else:
                    temp = ListNode(next1.val + next2.val + lead - 10, None)
                    lead = 1
                next1 = next1.next
                next2 = next2.next
                
            elif next1 is None and next2 != None:
                if next2.val + lead < 10:
                    temp = ListNode(next2.val + lead, None)
                    lead = 0
                else:
                    temp = ListNode(next2.val+lead-10, None)
                    lead = 1
                next2 = next2.next
            elif next2 is None and next1 != None:
                if next1.val + lead < 10:
                    temp = ListNode(next1.val + lead, None)
                    lead = 0
                else:
                    temp = ListNode(next1.val+lead-10, None)
                    lead = 1
                next1 = next1.next
            else:
                temp = ListNode(1, None)
                lead = 0
            curr.next=temp
            curr=curr.next
        return lst
            
            
    
        
