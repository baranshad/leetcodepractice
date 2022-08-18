class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def helper(in1, in2):
            t1 = in1[-1]
            if in2[0] > t1[1]:
                in1.append(in2)  
            elif in2[0] <= t1[1]: 
                in1[-1] = [t1[0], max(t1[1],in2[1])]
            return in1
            
        intervals.sort()   
        if len(intervals) ==1 or intervals == []:
            return intervals 
            
        elif len(intervals) == 2:
            res2 = helper([intervals[0]], intervals[1])
            return res2
        
        else:
            res = helper([intervals[0]], intervals[1])
            for i in range(2, len(intervals)):
                helper(res, intervals[i])
            return res 