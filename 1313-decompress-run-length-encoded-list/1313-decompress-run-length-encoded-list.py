class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        odds = [nums[i] for i in range(len(nums)) if i % 2 ]
        events = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        print(odds, events)
        res = []
        for i in range(len(events)):
            res.extend([odds[i]]*events[i])
            
        return res