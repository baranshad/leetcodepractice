class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d= {}
        p = 0
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = i
            else:
                if abs(d[val]- i) <= k:
                    return True 
                d[val] = i

        return False 
                
            