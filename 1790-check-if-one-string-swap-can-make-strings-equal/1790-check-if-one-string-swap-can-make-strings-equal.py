class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d=0
        n=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                d+=1
                n.append(i)
        print(d)
        print(n)
        if d !=2 and d!= 0:
            return False 
        elif d == 0 or (d ==2 and s1[n[0]] == s2[n[1]] and s1[n[1]]==s2[n[0]]):
            return True 
                
            
  
        #if d!=2 and d!=0:
          #return (False)
        #if d==0 or (s1[n[0]]==s2[n[1]] and s2[n[0]]==s1[n[1]]):
          #return (True)