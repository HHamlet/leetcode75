from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# not fast solution
class Solution:          
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        tail = ListNode(val=head.val)
        while temp.next:
            temp = temp.next
            tail = ListNode(val=temp.val,next=tail)
        return tail
    