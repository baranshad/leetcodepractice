class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for i in range(1, n+1):
            digits = sum(int(c) for c in str(i))
            d[digits] += 1 
        res = [i for i,j in d.items() if j == max(d.values())]
        return len(res)
        
        
        
        
      
        #maxCount = max(counts.values())
        #return sum(count == maxCount for count in counts.values())