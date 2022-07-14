class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mind = inf
        idx = cur = 0
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y: 
                cur = abs(x-points[i][0]) + abs(y-points[i][1])
                #print(cur)
                if cur < mind:
                    mind = cur 
                    idx = i 
        if mind == inf:
            return -1 
        else:
            return idx 
        #print(idx)
        
        
        #cur_index = 0
        #cur_min_man = 99999
        #man = 0
        #for i in range(len(points)):
            #if x == points[i][0] or y == points[i][1]:
                #val = (abs(x - points[i][0]) + abs(y - points[i][1]))
                #if cur_min_man > val:
                    #cur_min_man = val
                    #cur_index = i
                
        #if cur_min_man == 99999:
            #return (-1)
        #else:
            #return (cur_index)