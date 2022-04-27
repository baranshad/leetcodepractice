class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        ans = []
        for i in range(len(heights)-1,-1,-1):
            while res and heights[res[-1]] < heights[i]:
                res.pop()
            if not res:
                ans.append(i)
                
            res.append(i)

        return ans[::-1]
            