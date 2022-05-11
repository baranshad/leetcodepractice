class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(s=[], l=0, r=0):
            if len(s) ==2*n:
                ans.append("".join(s))
                
            if l < n:
                s.append("(")
                helper(s, l+1, r)
                s.pop()
                
            if r < l:
                s.append(")")
                helper(s, l, r+1)
                s.pop()
                
        helper()
        return ans 
                    