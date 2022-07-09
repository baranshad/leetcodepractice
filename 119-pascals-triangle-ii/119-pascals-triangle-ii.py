class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        ans = [[1]]
        for i in range(1, rowIndex+1):
            temp = [1]
            for j in range(1, i):
                temp.append(ans[i-1][j]+ans[i-1][j-1])
            temp.append(1)
            ans.append(temp)
            
        return ans[-1]
    
    
    
    
    
    