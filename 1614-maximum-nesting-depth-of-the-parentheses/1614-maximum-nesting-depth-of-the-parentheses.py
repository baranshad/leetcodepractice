class Solution:
    def maxDepth(self, s: str) -> int:
        ans = count = 0 
        for i in s:
            if i == "(":
                count += 1 
            elif i == ")":
                count -= 1 
            ans = max(count, ans)
        print(ans)
        return ans 