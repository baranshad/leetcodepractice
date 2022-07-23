class Solution:
    def modifyString(self, s: str) -> str:
        ans=list(s)  
        abc = set(['a','b','c'])
        for i, c in enumerate(ans):
            if c == "?":
                neib = set()
                if i != 0:
                    neib.add(ans[i-1])
                if i != len(ans)-1:
                    neib.add(ans[i+1])
                ans[i]=(abc - neib).pop()
        
        return "".join(ans)
    
    
        #s = list(s)
        #abc = set(['a','b','c'])
        #for i, c in enumerate(s):
            #if c == '?':
                #neib = set()
                #if i != 0:
                    #neib.add(s[i-1])
               # if i != len(s)-1:
                    #neib.add(s[i+1])
                #s[i] = (abc-neib).pop()
        #return "".join(s)