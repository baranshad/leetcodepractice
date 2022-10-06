class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        s= nums * 2 
        res = [-1]*len(s)
        stack = []
        
        for i, c in enumerate(s):
            while stack and s[stack[-1]] < c:
                res[stack.pop()] = c 
            stack.append(i)
            
        print(res)
        return res[:len(nums)]