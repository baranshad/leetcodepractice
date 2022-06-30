class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        c_sort = sorted(c.items(), key=lambda x: x[1], reverse=True )
        f_max = c_sort.pop(0)[1]
        idlenum = (f_max -1 )*n 
        print(c_sort)
        while c_sort and idlenum > 0 :
            idlenum -= min(f_max-1, c_sort.pop(-1)[1])
            
        idle_left = max(0, idlenum)
        return idle_left + len(tasks)
        