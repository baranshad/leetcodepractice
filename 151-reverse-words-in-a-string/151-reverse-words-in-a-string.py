class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0 
        r = len(s)-1
        
        while l <= r and s[l]==" ":
            l += 1 
            
        while l <= r and s[r]==" ":
            r -= 1 
        
        snew = s[l:r+1] + " "
        #print(snew[-1])
        ans = []
        temp = ""
        for i, char in enumerate(snew):
            if char == " ":
                if temp:
                    ans.append(temp)
                    temp = ""
            else:
                temp += char
                
        return ' '.join(ans[::-1])
                
            