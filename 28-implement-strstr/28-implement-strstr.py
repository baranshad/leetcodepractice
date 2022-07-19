class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1 
        for i, char in enumerate(haystack):
            if needle == haystack[i:i+len(needle)]:
                return i 
        return -1 