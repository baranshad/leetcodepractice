class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            n = target - val 
            if n in d:# 这一步很重要，如果没有这一步，
                ## 【3，2，4】 的情况，会出现【0，0】的结果，当d = {3: 0} 之后
                ## 这时候 6-3 = 3， 出现在d里面，会返回 【0，0】
                return [d[n],i]
            
            else:
                d[val] = i
                
      