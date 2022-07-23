class Solution:
    def reformatNumber(self, number: str) -> str:
        c = ''.join([i for i in number if 48<=ord(i)<=57])
        ans =[]
        
        while True:
            if len(c) > 4:
                ans.append(c[:3])
                c = c[3:]
            else:
                if len(c) == 2:
                    ans.append(c[:2])
                    c = c[2:]
                if len(c) == 3:
                    ans.append(c[:3])
                    c = c[3:]
                if len(c) == 4:
                    ans.append(c[:2])
                    ans.append(c[2:])
                    c = ""
            if len(c)==0:
                break
                
        return '-'.join(ans)
    
    
    
   