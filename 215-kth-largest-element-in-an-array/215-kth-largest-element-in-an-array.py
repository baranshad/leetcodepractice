class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums[:k]
        res.sort()
        for i in nums[k:]: 
            if res[0] >= i:
                continue 
            else:
                res.pop(0)
                res.append(i)
                res.sort()
            
        print(res)
        return res[0]
 
         
