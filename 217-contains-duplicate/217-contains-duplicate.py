class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for val in nums:
            if val not in d:
                d[val] = 1 
            else:
                return True
        return False