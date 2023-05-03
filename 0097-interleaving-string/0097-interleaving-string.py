class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 

        def helper(l1, l2, temp):
            if l1 >= len(s1) or l2 >= len(s2):
                return s1[l1:] + s2[l2:] == s3[l1+l2:]
            
            if (l1, l2) in temp:
                return temp[(l1, l2)]
            
            ans = False 
            if (s1[l1]==s3[l1+l2] and helper(l1+1, l2, temp)) or (s2[l2]==s3[l1+l2] and helper(l1, l2+1, temp)):
                ans = True 
                
            temp[(l1,l2)] = ans 
            return ans 
        
        
        return helper(0,0,{})



           