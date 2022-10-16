class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        res = 0 
        for t in time:
            if t % 60 ==0:
                res += d[0]
            else:
                res += d[60-t%60]
            d[t%60] += 1 
            
        return res 