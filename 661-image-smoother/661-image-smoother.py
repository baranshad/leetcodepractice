class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        d= [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        m = len(img)
        n = len(img[0])
        ans = [[0]*n for i in range(m)] 
        for i in range(m):
            for j in range(n):
                temp = [img[i+r][j+c] for r,c in d if 0<= i+r < m and 0<= j+c < n]
                ans[i][j] = sum(temp)//len(temp)
                
        return ans 