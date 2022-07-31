class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        cnt = 1
        dic = {}
 
        for i in reversed(sorted(score)):
            if cnt == 1:
                dic[i] = "Gold Medal"
            elif cnt == 2:
                dic[i] = "Silver Medal"
            elif cnt == 3:
                dic[i] = "Bronze Medal"
            else:
                dic[i] = str(cnt)
            cnt += 1
        return [dic[i] for i in score]
         