class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)
        i = 0
        while i < len(s) -1:
            if s[i][1] >= s[i+1][0]:
                #s[i][1] = max(s[i][1], s[i+1][1])
                s[i] = [s[i][0], max(s[i][1], s[i+1][1])]
                s.pop(i+1)
            else:
                i += 1
        return s


