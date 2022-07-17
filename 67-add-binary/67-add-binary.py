class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry, res = len(a)-1, len(b)-1, 0, ""
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry%2) + res
            carry //= 2
        return res
         
            
       # i, j, carry, res = len(a)-1, len(b)-1, 0, ""
    #while i >= 0 or j >= 0 or carry:
        #if i >= 0:
            #carry += int(a[i])
            #i -= 1
        #if j >= 0:
            #carry += int(b[j])
            #j -= 1
        #res = str(carry%2) + res
        #carry //= 2
    #return res    
            
        #final_int, final_str, carry = str(int(a) + int(b)), "", 0
        
        #for i in range(len(final_int)-1,-1,-1):
            #temp_val = int(final_int[i]) + carry
            #val = temp_val % 2  
            #carry = temp_val // 2
            #final_str += str(val)
        
        #if carry:
           # final_str += "1"
        
        #return final_str[::-1]