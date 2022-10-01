class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
            
        def dfs(i):
            visited.add(i)
            for nb in d[i]:
                if nb not in visited:
                    visited.add(nb)
                    dfs(nb)
        
        visited = set()
        counter = 0 
        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1 
                
        return (counter)        
        
  