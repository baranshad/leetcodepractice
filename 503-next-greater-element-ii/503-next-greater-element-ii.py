class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        s = nums*2 
        print(s)
        stack = []
        res = [-1]*len(s)
        for idx, i in enumerate(s):
            while stack and s[stack[-1]] < i:
                res[stack.pop()] = i
            stack.append(idx)
            
                    
        return res[:len(nums)]
                
            
                