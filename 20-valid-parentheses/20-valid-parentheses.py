class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        d = {"(":")", "[":"]","{":"}"}
        leftd = {"(", "[", "{"}
        for c in s:
            if c in leftd:
                left.append(c)
            elif left and c == d[left[-1]]:
                left.pop()
            else:
                return False         
        return not left  