class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0 
        i = len(num1)-1
        j = len(num2)-1
        res = []
        while i >= 0 or j >= 0:
            x1 = int(num1[i]) if i >= 0 else 0
            x2 = int(num2[j]) if j >= 0 else 0
            value = (x1 + x2 + carry) % 10 
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            i -= 1 
            j -= 1 
            
        if carry:
            res.append(carry)
            
            
        return "".join(str(x) for x in res[::-1])
            
        