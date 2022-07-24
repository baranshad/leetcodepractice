class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return 
        stack = []
        d= {}
        for i in  nums2:
            while stack and i > stack[-1]:
                d[stack.pop()] = i
                #print(d)
            stack.append(i)  
        res = [d.get(i, -1) for i in nums1]
        return res 