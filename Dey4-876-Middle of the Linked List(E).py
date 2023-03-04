# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_lenght = 0
        cnt =0
        temp = head
        while temp:
            list_lenght +=1
            temp = temp.next
        while head:
            if cnt == list_lenght//2:
                return head
            else:
                cnt +=1
                head = head.next
        return None
        