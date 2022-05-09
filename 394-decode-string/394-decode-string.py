class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = 0 
        
        for i in s:
            if i.isdigit():
                number = number*10 + int(i)
                
            elif i == "[":
                stack.append(number)
                number = 0
                
            elif i == ']':
                strs = []
                while stack and not isinstance(stack[-1], int):
                    strs.append(stack.pop())
                strs.reverse()
                repeatenumber = stack.pop()
                for _ in range(repeatenumber):
                    stack.append(''.join(strs))
            else:
                stack.append(i)
                    
        strs = []
        while stack:
            strs.append(stack.pop())
        strs.reverse()
        return ''.join(strs)