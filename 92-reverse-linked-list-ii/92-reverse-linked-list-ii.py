# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        
        start = dummy 
        for _ in range(left-1):
            start = start.next 
        
        prev = None 
        cur = start.next 
        for _ in range(right-left+1):
            temp = cur.next 
            cur.next = prev 
            prev = cur 
            cur  = temp 
        start.next.next=cur
        start.next = prev 
        
        return dummy.next 