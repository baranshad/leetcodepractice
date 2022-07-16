class Solution:
    def toLowerCase(self, s: str) -> str:
        isupper = lambda x: 'A' <= x <= 'Z'
        islower = lambda x: chr(ord(x) | 32)
        return ''.join([islower(x) if isupper(x) else x for x in s])