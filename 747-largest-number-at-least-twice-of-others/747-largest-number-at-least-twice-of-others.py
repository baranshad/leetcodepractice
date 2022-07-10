class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sn = {}
        for i, val in enumerate(nums):
            sn[val] = i
        lists = sorted(sn.items(), key=lambda x:x[0], reverse=True)
        if lists[0][0] >= 2* lists[1][0]:
            return lists[0][1] 
        return -1