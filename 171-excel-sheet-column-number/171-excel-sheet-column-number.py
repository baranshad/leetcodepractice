class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}
        n = len(columnTitle)
        for i in range(n):
            cur = columnTitle[n-1-i]
            result += (alpha_map[cur] * (26 ** i))
        
        return result