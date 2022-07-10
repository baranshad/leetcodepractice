class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxnum = set()
        for i in nums:
            maxnum.add(i)
            if len(maxnum) > 3:
                maxnum.remove(min(maxnum))
        
        if len(maxnum) == 3:
            return min(maxnum)
        
        return max(maxnum)
        
        
        
        