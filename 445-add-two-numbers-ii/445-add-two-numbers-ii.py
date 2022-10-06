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
            #print(add1)
            add2 = s2.pop() if s2 else 0 
            val1 = (add1 + add2 + carry)%10
            carry = (add1 + add2 + carry)//10
            
            cur = ListNode(val1)
            cur.next = dummy.next 
            dummy.next =cur 
        
        return cur
            