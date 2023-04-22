# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = ListNode()
        slow.next = head 
        cur = slow 
        fast = head 

        while fast and fast.next:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next 

            if cur.next == fast:
                cur = fast 
            elif cur.next != fast:
                cur.next = fast.next 
            fast = fast.next 
        return slow.next 


 
            