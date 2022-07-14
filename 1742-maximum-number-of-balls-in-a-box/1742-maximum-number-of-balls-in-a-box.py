class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res = []
        for i in range(lowLimit, highLimit+1):
            res.append(sum([int(x) for x in str(i)]))
        ans = Counter(res)
        print(ans)
        ans1 = [j for i,j in ans.items() if j == max(ans.values())]
        return ans1[0]