class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(s, l, r):
            if len(s) == 2*n:
                ans.append("".join(s))
            if l < n:
                s.append("(")
                helper(s, l+1, r)
                s.pop()
                
            if r < l:
                s.append(")")
                helper(s, l, r+1)
                s.pop()
                
            return ans 
        
        helper([], 0,0)
        return ans 
                