class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def helper(temp, idx):
            if temp[-1] == len(graph) -1:
                ans.append(temp[:])
                
            nbs = graph[idx]
            for i in nbs:
                temp.append(i)
                helper(temp, i)
                temp.pop()
                
        helper([0],0)
        return ans 
    
                    
                