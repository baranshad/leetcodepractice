class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        
        
        def helper(i):
            for nb in d[i]:
                if nb not in visited:
                    visited.add(nb)
                    helper(nb)
                
        visited = set()
        counter = 0 
        for i in range(n):
            if i not in visited:
                visited.add(i)
                helper(i)
                counter +=1 
                
        return counter 

    