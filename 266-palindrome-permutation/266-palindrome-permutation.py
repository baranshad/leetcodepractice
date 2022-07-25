class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        return sum(j % 2 for j in c.values()) < 2