class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c1 = Counter(nums)
        c2 = [i for i, j in c1.items() if j >= 2]
        return c2[0]