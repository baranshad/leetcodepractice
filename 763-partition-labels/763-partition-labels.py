class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## hash map return max idx each char can reach 
        d = {}
        for i,c in enumerate(s):
            d[c] = i
            
        res =[]
        l = r = 0 
        for i, char in enumerate(s):
            r = max(r, d[char])
            if i == r:
                res.append(r-l+1)
                l = r + 1 
        return res 