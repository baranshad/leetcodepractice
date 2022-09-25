class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        ope = "+"
        stack = []
        for i, val in enumerate(s):
            if val.isnumeric():
                num = num*10 + int(val)
                print(num)
            if val in '+-*/' or i == len(s) -1:
                if ope == "+":
                    stack.append(num)
                elif ope =="-":
                    stack.append(-num)
                elif ope == "*":
                    j = num*(stack.pop())
                    stack.append(j)
                elif ope == "/":
                    j = int(stack.pop()/num)
                    stack.append(j)
                    
                ope = val 
                num = 0 
        return sum(stack)
                