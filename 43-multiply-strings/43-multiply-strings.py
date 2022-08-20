class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def helper(num1, val):
            carry = 0 
            ans = []
            for i in num1[::-1]:
                cur = int(i) * val + carry 
                carry = cur// 10 
                ans.append(cur%10)
            if carry:
                ans.append(carry)  
            res = 0
            for i in range(len(ans)-1, -1, -1):
                res += ans[i]*(10**i)
            return res
        
        res = 0
        for i, val in enumerate(num2[::-1]):
            res += helper(num1, int(val)) * (10**i)
            
        return str(res)