class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            res = []
            for i in string:
                if i != "#":
                    res.append(i)
                elif res:
                    res.pop()
            return res 
        
        return helper(s) == helper(t)