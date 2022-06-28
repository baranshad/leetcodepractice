class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        if k == 0:
            temp = Counter(nums_sorted)
            return len({key: value for key, value in temp.items() if value > 1})
        count = 0
        for i in range(len(nums)-1):
            if nums_sorted[i] != nums_sorted[i+1] and nums_sorted[i] + k in nums_sorted:
                count += 1 
                
        return count 