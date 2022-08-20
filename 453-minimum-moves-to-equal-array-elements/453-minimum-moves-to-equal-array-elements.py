class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sumnums = sum(nums)
        return sumnums - (min(nums)* len(nums))