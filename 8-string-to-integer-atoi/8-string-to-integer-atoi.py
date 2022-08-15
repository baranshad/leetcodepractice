class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        result = j = 0
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        while j < len(s) and s[j] == " ":
            j += 1 
            
        if j < len(s) and s[j] == "+":
            sign = 1 
            j += 1 
            
        elif j < len(s) and s[j] == "-":
            sign = -1 
            j += 1 
            
            
        while j < len(s) and s[j].isdigit():
            digit = int(s[j])
            
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):    
                return INT_MAX if sign == 1 else INT_MIN
            
            result = 10* result + digit 
            j += 1 
            
        return sign * result 