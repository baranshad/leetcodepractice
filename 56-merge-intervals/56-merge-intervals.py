class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        t1 = sorted(intervals)
        
        i = 0 
        while i < len(t1) - 1:
            if t1[i][1] >= t1[i+1][0]:
                t1[i][1] = max(t1[i][1],t1[i+1][1])
                t1.pop(i+1)
            else:
                i+=1

        return t1 
