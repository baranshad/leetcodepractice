class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i, j in prerequisites:
            d[i].append(j)
            
        for k in range(numCourses):
            q = deque(d[k]) # 1,2,3,0
            seen = set()
            while q: ## 3
  # [[0,2], [0,1],[2,1]] is true 
  ##.  0 
  ## 1   2 
  ##     1  if here 1 can back to 0 then cycle 
                m = q.pop()  
                if m == k: # if k = 0, then when met 0 there is a cycle 
                    return False 
                seen.add(m)  ## if no circle, add to seen classes 
                for nb in d[m]:  ## go dfs, to the nbs of the class
                    #print(seen, nb)
                    if nb not in seen: ## if not seen then append 
                        q.append(nb)
                        #print(q)
            print(seen)
        return True 