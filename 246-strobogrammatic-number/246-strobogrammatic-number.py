class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        r = []
        for i in reversed(num):
            if i not in rotated_digits:
                return False 
            r.append(rotated_digits[i])
            
        res = "".join(r)
        return res == num