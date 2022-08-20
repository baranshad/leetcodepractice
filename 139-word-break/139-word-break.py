class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w = set(wordDict)
        can = [False]*(len(s)+1)
        can[0] = True 
        print(can)
        for i in range(1, len(s)+1):
            for j in range(i):
                if can[j] and s[j:i] in w:
                    can[i] = True 
                    #break 
        return can[-1]