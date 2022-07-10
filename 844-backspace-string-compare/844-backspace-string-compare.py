class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            ans = []
            for i in s:
                if i != "#":
                    ans.append(i)
                elif ans:
                    ans.pop()
            return "".join(ans)
        
        return helper(s) == helper(t)