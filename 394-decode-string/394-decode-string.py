class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "[":
                stack.append(num)
                num = 0 
                
            elif i == "]":
                str1 = []
                while stack and not isinstance(stack[-1], int):
                    str1.append(stack.pop())
                str1.reverse()
                repeatnum = stack.pop()
                for _ in range(repeatnum):
                    stack.append("".join(str1))
            else:
                stack.append(i)
                
        return ("".join(stack))