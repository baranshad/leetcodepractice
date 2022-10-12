class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = {}
        for i in s:
            if i in s_counter:
                s_counter[i] += 1 
            else:
                s_counter[i] = 1 

        

        charleft = ""
        maxfreq = 0
        ans = ["@"]
        
        for i in range(len(s)):
            for j, c in s_counter.items():
                if c > maxfreq and j != ans[-1]:
                    charleft = j 
                    maxfreq = c 
                    
            if charleft == "":
                return ""
            
            s_counter[charleft] = s_counter[charleft] -1 
            ans.append(charleft)
            maxfreq = 0
            charleft = ""
            
        return "".join(ans[1:])