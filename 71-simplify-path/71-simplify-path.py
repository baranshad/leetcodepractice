class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for s in arr:
            if s == '..':
                if stack:
                    stack.pop()
                    
            elif s=='.' or s=='':
                continue 
                
            else:
                stack.append(s)
                
        if not stack:
            return '/'
        
        string = ''
        while stack:
            string = '/' + stack.pop() + string 
            
        return string 