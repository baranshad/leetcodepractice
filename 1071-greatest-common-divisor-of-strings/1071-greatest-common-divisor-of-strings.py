class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 + str1 != str1 + str2:
            return ""
        
        def gcd(x,y):
            if y ==0:
                return x 
            return gcd(y, x%y)
        
        val = gcd(len(str1), len(str2))
        return str2[:val]