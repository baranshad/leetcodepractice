class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ns = sorted(nums)
        return max(ns[0]*ns[1]*ns[-1], ns[-1]*ns[-2]*ns[-3])