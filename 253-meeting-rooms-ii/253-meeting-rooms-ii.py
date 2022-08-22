class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        for start, end in intervals:
            rooms.append((start, True))
            rooms.append((end, False))
            
        rooms.sort()
        res = count = 0
        for i, flag in rooms:
            if flag:
                count +=1 
            else:
                count -=1 
            res = max(res, count)
        return res 
 