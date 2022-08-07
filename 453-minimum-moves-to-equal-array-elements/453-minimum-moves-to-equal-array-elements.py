class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sumall = sum(nums)
        return sumall - len(nums)*(min(nums))