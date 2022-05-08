# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next 
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next 
            
        
        dummy = ListNode(0)
        carry = 0 
        while s1 or s2 or carry:
            add1 = s1.pop() if s1 else 0 
            add2 = s2.pop() if s2 else 0 
            sum1 = add1 + add2 + carry 
            carry = 1 if sum1 >= 10 else 0
            sum1 = sum1 -10 if sum1 >= 10 else sum1 
            
            cur = ListNode(sum1)
            cur.next = dummy.next 
            dummy.next = cur 
            
        return dummy.next
            