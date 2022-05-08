# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next =head 
        
        start = dummy 
        for i in range(left-1):
            start = start.next 
            
        prev = None 
        current = start.next
        for j in range(right-left+1):
            third = current.next 
            current.next = prev 
            prev = current 
            current = third 
            
        start.next.next = current 
        start.next = prev 
        
        return dummy.next 