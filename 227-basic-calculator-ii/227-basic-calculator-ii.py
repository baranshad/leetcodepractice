class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+"
        current = 0 
        outer = 0
        result = 0
        operature = "+"
        for c in s:
            if c == " ":
                continue 
            if c.isdigit():
                current = 10* current + int(c)
                continue 
            if operature == "+":
                result += outer 
                outer = current 
            elif operature == "-":
                result += outer 
                outer = -current 
            elif operature == "*":
                outer = outer * current 
            elif operature == "/":
                outer = int(outer/current)
                
            current, operature = 0, c 
            
        return result + outer 