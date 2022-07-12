class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, j in zip(nums,index):
            res.insert(j,i)
            
        return res 