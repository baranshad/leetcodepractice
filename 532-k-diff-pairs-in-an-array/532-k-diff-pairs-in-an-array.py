class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums1 = sorted(nums)
        if k == 0:
            temp = Counter(nums1)
            return len([i for i, j in temp.items() if j >1])
        
        count = 0 
        for i in range(len(nums)-1):
            if nums1[i] != nums1[i+1] and nums1[i]+k in nums1:
                count += 1 
                
        return count 