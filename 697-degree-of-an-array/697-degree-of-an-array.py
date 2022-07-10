class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, val in enumerate(nums):
            d[val].append(i)

        d_s = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
        res = [j for i, j in d_s if len(j) == len(d_s[0][1])]
        #print(res)
        ans = [max(i)-min(i) +1 for i in res]
        print(ans)
        return min(ans)