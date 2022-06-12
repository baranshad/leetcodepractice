# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        pre = dummy 
        
        while head and head.next:
            s = head 
            f = head.next 
            
            pre.next = f
            s.next = f.next 
            f.next =s 
            
            pre = s 
            head = s.next 
            
        return dummy.next 