class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return 
        d= {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()] = i 
            stack.append(i)
        
        res = [d.get(i, -1) for i in nums1]
        return res 
         
            