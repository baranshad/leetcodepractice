class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0 
        ope = "+"
        
        for i, val in enumerate(s):
            if val.isnumeric():
                num = num*10 + int(val)
            
            if val in "+-*/" or i == len(s)-1:
                #print(i, val, stack, num)
# 3+4*2
# +3+ 4*2 
#1 + [] 3
#3 * [3] 4
#4 2 [3, 4] 2

                if ope == "+":
                    stack.append(num)
                elif ope == "-":
                    stack.append(-num)
                elif ope == "*":
                    j = stack.pop() * num 
                    #print(j) # 8 
                    stack.append(j)
                elif ope == "/":
                    j = stack.pop()/num 
                    stack.append(int(j))
                    
                num = 0 
                ope = val
                
        return sum(stack)