# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = ListNode(0)
        curr = res
        while l1 or l2 or carry:
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0
            allsum = x + y + carry 
            carry = (allsum) //10 
            val = ListNode((allsum) % 10)
            curr.next = val
            curr = val 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return res.next