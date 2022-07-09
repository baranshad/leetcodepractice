class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        d = {"(":")", "[":"]","{":"}"}
        for c in s:
            if c in d:
                left.append(c)
            elif left and c == d[left[-1]]:
                left.pop()
            else:
                return False         
        return not left  