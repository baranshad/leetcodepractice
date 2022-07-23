class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        maxlen = -1
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                maxlen = max(maxlen, i-(d[c]+1))
        return maxlen