class Solution:
    def addBinary(self, a: str, b: str) -> str:
        added = str(int(a)+ int(b))
        res = ""
        carry = 0 
        for i in range(len(added)-1, -1, -1):
            val = (int(added[i]) + carry) % 2 
            carry = (int(added[i]) + carry) // 2 
            res += str(val)
        
        if carry:
            res = res + "1"
        return res[::-1]

        #final_int, final_str, carry = str(int(a) + int(b)), "", 0
        
        #for i in range(len(final_int)-1,-1,-1):
            #temp_val = int(final_int[i]) + carry
            #val = temp_val % 2  
            #carry = temp_val // 2
            #final_str += str(val)
        
        #if carry:
           # final_str += "1"
        
        #return final_str[::-1]