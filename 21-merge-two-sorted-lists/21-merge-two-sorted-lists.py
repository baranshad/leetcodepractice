# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = dummy = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1 
                list1 = list1.next 
            else:
                pre.next = list2 
                list2 = list2.next 
            pre = pre.next 
        pre.next = list1 or list2 
        return dummy.next 