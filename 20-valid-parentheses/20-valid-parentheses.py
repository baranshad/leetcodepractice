class Solution:
    def isValid(self, s: str) -> bool:
        cdict = {'(': ')', '{' :'}' ,'[': ']'}
        stack = []
        for c in s:
            if c in cdict:
                stack.append(c)
            elif stack and cdict[stack[-1]] == c:
                stack.pop()
            else:
                return False 
                
        return stack == []