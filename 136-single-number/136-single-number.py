class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = Counter(nums)
        ss = sorted(s.items(), key = lambda x: x[1])
        return ss[0][0]