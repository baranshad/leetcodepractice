class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return 
        
        stack = []
        next_g_map = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_g_map[stack.pop()] = num 
                
            stack.append(num)
            
        return [next_g_map.get(num, -1) for num in nums1] 


  
            
        