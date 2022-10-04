class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
                
            elif i == "[":
                stack.append(num)
                num = 0 
                
            elif i == "]":
                
                strs = []
                while stack and not isinstance(stack[-1], int):
                    strs.append(stack.pop())
                strs.reverse()
                repeatimes = stack.pop()
                for _ in range(repeatimes):
                    stack.append("".join(strs))
                    
            else:
                stack.append(i)
                
        return ("".join(stack))