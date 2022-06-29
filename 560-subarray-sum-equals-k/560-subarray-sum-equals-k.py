class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = defaultdict(int)
        presum[0] = 1
        temp = 0
        ans = 0
        for i in range(len(nums)):
            temp += nums[i]
            #if temp == k:
                #ans += 1 
            if temp - k in presum:
                ans += presum[temp-k]
            presum[temp] += 1 
        print(presum)
        return ans 
            