class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t1 = collections.Counter(nums)
        #t2 = sorted(t1.items(), key=lamda x: x[1], reverse = True)
        num = int(len(nums)/3)
        return [i for i, j in t1.items() if j > num]
        
