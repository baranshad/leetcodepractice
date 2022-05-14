class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list) # create adjacency list
        for i, j in prerequisites:
            d[i].append(j)
                        
        for n in range(0,numCourses):
            Q = deque(d[n])
            visited = set()
            while Q:
                #m = Q.popleft()  # --> BFS
                m = Q.pop()     # --> DFS
                if m==n:
                    return False # we detected a loop
                visited.add(m)  
                for nb in d[m]:
                    if nb not in visited:
                        Q.append(nb)
        
        return True