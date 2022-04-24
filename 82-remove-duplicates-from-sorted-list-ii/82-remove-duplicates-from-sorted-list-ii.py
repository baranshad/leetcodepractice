# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        slow = ListNode()
        slow.next = head 
        fast = head 
        pre = slow
        while fast and fast.next:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if pre.next == fast:
                pre = pre.next 
            elif pre.next != fast:
                pre.next = fast.next 
            fast = fast.next 
            
        return slow.next 
            
            