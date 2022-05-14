class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        d = defaultdict(list)
        for i, j in prerequisites:
            d[i].append(j)
            #graph[b].append(a)  # no, because graph is directional!
                        
        for n in range(0,numCourses):
            Q = deque(d[n])
            #res = []
            visited = set()
            while Q:
                #m = Q.popleft()  # --> BFS
                m = Q.pop()     # --> DFS
                if m==n:
                    return False # we detected a loop
                visited.add(m)  # this is just for optimization, not strictly needed
                for neighbor in d[m]:
                    if neighbor not in visited:
                        Q.append(neighbor)
        
        return True