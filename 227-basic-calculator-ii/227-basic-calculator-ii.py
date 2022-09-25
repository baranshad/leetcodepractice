class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0 
        ope = "+"
        
        for i,c in enumerate(s):
            if c.isnumeric():
                num = num*10 + int(c)
            if c in "+-*/" or i == len(s) -1:
                if ope == "+":
                    stack.append(num)
                elif ope == "-":
                    stack.append(-num)
                elif ope == "*":
                    j = stack.pop() * num 
                    stack.append(j)
                elif ope == "/":
                    j = stack.pop()/num
                    stack.append(int(j))
                
                num = 0 
                ope = c

        return sum(stack)