# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = prev = ListNode()
        cur.next= head
        
        
        for i in range(left-1):
            cur = cur.next
        #print(cur)   
        dummy = None
        first = cur.next 
        for i in range(right-left+1):
            temp = first.next 
            first.next = dummy
            dummy = first 
            first = temp 
        print(first)   #[1,2,3,4,5] left = 2, right = 4 need [1,4.3,2,5]
        print(dummy) # first = 5 , dummy = 4
        #print(cur)
        cur.next.next = first ## previous cur = 1, cur.next = 2 so cur.n3xt point to 5 
        cur.next = dummy ## cur.next point to 4 
        
        
        return prev.next
            
        
            
            