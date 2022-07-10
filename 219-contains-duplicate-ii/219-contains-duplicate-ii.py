class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        prev = 0
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = i 
            else:
                prev = d[v]
                d[v] = i 
                if abs(i-prev) <= k:
                    return True 
                
        return False 