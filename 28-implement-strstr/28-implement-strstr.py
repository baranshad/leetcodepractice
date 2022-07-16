class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        for j in range(len(haystack)):
            if haystack[j:j+len(needle)] == needle:
                return j
        return -1 