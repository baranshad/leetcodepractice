# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head 
        for i in range(n):
            fast = fast.next 
        if not fast: ## corner case here, why return head.next 
            return head.next
        slow = head 
        while slow and fast.next:
            fast = fast.next 
            slow = slow.next 
        slow.next = slow.next.next 
        return head ## why not as above return head.next 
        
        
      
         
        