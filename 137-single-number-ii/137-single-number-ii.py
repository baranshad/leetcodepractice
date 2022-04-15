class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = collections.Counter(nums)
        t2= sorted(tmp.items(), key=lambda x: x[1], reverse=False)
        return t2[0][0]