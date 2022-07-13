class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = Counter(nums)
        d_2 = [j for j in d.values() if j > 1]
        print(d_2)
        res = 0
        for i in d_2:
            res += i*(i-1) /2 
        return int(res) 