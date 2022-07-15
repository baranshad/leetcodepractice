class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        s1 = s + " "
        end = len(s1)-1
        temp = ""
        i = 0
        while i <= end:
            if s1[i] == " " or i == end:
                r = "".join(reversed(s1[start:i+1]))
                temp = temp + r
                i += 1 
                start = i
            else: 
                i += 1 
        return temp[1:] 
        
        
     #   a=s+" "
#l,e=0,len(a)-1
#i=0
#t=""
#while i<=e:
#if a[i]==" " or i==e:
#r= "".join(reversed(a[l:i+1]))
#t=t+r
#i+=1
#l=i
#else:
#i=i+1
#return t[1:]
                 
        
        
                