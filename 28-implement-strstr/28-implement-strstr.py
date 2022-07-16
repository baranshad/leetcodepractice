class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        #i=0
        for j in range(len(haystack)):
            if haystack[j:j+len(needle)] == needle:
                return j