class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        print(c)
        ans = -1
        for i, j in c.items():
            if i==j:
                ans = max(ans, i)
        return ans 
       
  