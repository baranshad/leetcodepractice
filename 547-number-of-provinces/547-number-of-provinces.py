class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def helper(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    if j not in visited:
                        visited.add(j)
                        helper(j)
                        
        count = 0
        visited=set()
        for i in range(len(isConnected)):
            if i not in visited:
                count +=1 
                helper(i)
                
        return count 

        