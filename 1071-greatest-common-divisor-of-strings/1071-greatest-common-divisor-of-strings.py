class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(i, j):
            if j ==0:
                return i 
            return gcd(j, i%j)
        
        if str1 + str2 != str2 + str1:
            return ""
        
        val = gcd(len(str1), len(str2)) 
        #print(val)
        return str1[:val]      
