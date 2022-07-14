class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = [i for i,j in c.items() if j == 1]
        return sum(res)