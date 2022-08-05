class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        strk = [int(i) for i in str(k)]
        i = len(num)-1
        j = len(strk) - 1 
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            x1 = num[i] if i >=0 else 0
            x2 = strk[j] if j >=0 else 0
            val = (x1 + x2 + carry) % 10 
            carry = (x1 + x2 + carry)// 10 
            res.append(val)
            i -= 1 
            j -= 1 
        
        if carry:
            res.append(carry)
        
        return res[::-1]
            
            