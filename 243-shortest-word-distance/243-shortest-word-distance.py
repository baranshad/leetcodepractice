class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        left = float('inf')
        right = float('inf')
        res = float('inf')
        for i, v in enumerate(wordsDict):
            if v == word1:
                left = i 
            elif v == word2:
                right = i 
            res = min(abs(right-left), res)
        return res 
        