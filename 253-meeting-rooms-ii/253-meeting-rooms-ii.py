class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        for s, e in intervals:
            rooms.append((s, True))
            rooms.append((e, False))
        rooms.sort()
        num = 0
        res = 0
        for i, flag in rooms:
            if flag: num += 1 
            else: num -=1 
            
            res = max(res, num)
        return res 
        
        
        
        
        #res = [x for x in set(tuple(x) for x in intervals)]
        #s = sorted(res, key=lambda x: (x[0], x[1]))
        #d= defaultdict(list)
        
        #endlist = []
        #for i in range(len(res)):
            #d[i] = s[i][0]
            #endlist.append(s[i][1])
        #for k, j in enumerate(endlist):
            #for m in range(len(d)):
                #if d[m] >= j:
                    #endlist[k]=endlist[m]
                    #d.pop(m)
                    
        #return len(d) + (len(intervals)-len(res))
                    