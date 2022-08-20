class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i, j in prerequisites:
            d[i].append(j)
            
        for i in range(numCourses):
            q =deque(d[i])
            seen = set()
            while q:
                m = q.pop()
                if m == i:
                    return False 
                seen.add(m)
                for nb in d[m]:
                    if nb not in seen:
                        q.append(nb)
        return True 
                