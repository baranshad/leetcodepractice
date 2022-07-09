class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 0: return []
        ans = [[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(ans[i-1][j]+ ans[i-1][j-1])
            temp.append(1)
            ans.append(temp)
        return ans 