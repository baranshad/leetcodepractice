class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)      
        ans = [i for i, j in d.items() if j ==1]
        if ans == []:
            return -1
        for i, char in enumerate(s):
            if char in ans:
                return i 
                break 
        return -1