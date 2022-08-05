class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        j = 1 
        d = {}
        for i in reversed(sorted(score)):
            if j == 1:
                d[i] = "Gold Medal"
            elif j==2:
                d[i] = "Silver Medal"
            elif j ==3:
                d[i] = "Bronze Medal"
            else:
                d[i] = str(j)
            j += 1
        return [d[i] for i in score]