class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        nums = code * 2 
        res = []
        if k==0: return len(code)*[0]
        elif k > 0: 
            for i in range(len(code)):
                res.append(sum(nums[i+1:i+k+1]))
        else:
            for i in range(len(code), len(nums)):
                res.append(sum(nums[i+k:i]))
        
        return res 