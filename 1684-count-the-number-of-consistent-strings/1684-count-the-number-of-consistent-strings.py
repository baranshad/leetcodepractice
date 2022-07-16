class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            if set(i) <= set(allowed):
                count +=1 
        return count 