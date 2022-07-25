class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        prev = 0 
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = i 
            else:
                prev = d[val]
                d[val] = i
                if abs(i-prev) <= k:
                    return True 
        return False 