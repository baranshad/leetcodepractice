class Solution:
    def addBinary(self, a: str, b: str) -> str:
        final_int = str(int(a) + int(b)) 
        final_str = "" 
        carry = 0
        for i in range(len(final_int)-1, -1, -1):
            val = (int(final_int[i]) + carry) % 2 
            carry = (int(final_int[i]) + carry) // 2 
            final_str += str(val)
        if carry:
            final_str += "1"
        return final_str[::-1]
         
      
            
        #final_int, final_str, carry = str(int(a) + int(b)), "", 0
        
        #for i in range(len(final_int)-1,-1,-1):
            #temp_val = int(final_int[i]) + carry
            #val = temp_val % 2  
            #carry = temp_val // 2
            #final_str += str(val)
        
        #if carry:
           # final_str += "1"
        
        #return final_str[::-1]