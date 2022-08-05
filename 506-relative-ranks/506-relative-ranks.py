class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        j = 1
        dic = {}
        for i in reversed(sorted(score)):
            if j == 1:
                dic[i] = "Gold Medal"
            elif j == 2:
                dic[i] = "Silver Medal"
            elif j==3:
                dic[i] = "Bronze Medal"
                
            else:
                dic[i] = str(j)
                
            j += 1 
            
        return [dic[i] for i in score]
         