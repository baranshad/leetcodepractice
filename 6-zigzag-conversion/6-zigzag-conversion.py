class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = position = 1 
        lines = {}
        for c in s:
            if position not in lines:
                lines[position] = c 
            else:
                lines[position] += c 
                
            position += step 
            if position == 1 or position == numRows:
                step *= -1 
        
        res = ""
        for i in range(1, numRows+1):
            try:
                res+= lines[i]
            except:
                return res 
            
        return res 