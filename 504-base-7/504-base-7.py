class Solution:
    def convertToBase7(self, num: int) -> str:
        
        def helper(num):
            res = ""
            abs_num = abs(num)
            while abs_num >=7:
                val = abs_num // 7 
                remainder = abs_num % 7 
                res += str(remainder)
                abs_num = val 
            res += str(abs_num)
            return res[::-1] 
        
        if num<0:
            ans = helper(num)
            return str(-int(ans))
        else:
            return helper(num)
        
        