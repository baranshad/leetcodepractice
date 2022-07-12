class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1 
            else:
                d[i] = 1 
        print(d)   
        res = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(res[0][0], res[0][1], len(nums)/2)
        return res[0][0] == target and res[0][1] > len(nums)/2