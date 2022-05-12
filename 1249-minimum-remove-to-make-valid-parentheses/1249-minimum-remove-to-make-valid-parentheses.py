class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toremove = set()
        stack = []
        for i, val in enumerate(s):
            if val not in "()":
                continue 
            elif val == "(":
                stack.append(i)
            elif not stack:
                toremove.add(i)
            else:
                stack.pop()
        toremove = toremove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in toremove:
                res.append(c)
        return "".join(res)
            
                
            