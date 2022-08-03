class Solution:
    def reformatNumber(self, number: str) -> str:
        c = "".join([i for i in number if i.isdigit()])
        res = []
        while True:
            if len(c) > 4:
                res.append(c[:3])
                c = c[3:]
            else:
                if len(c) == 2:
                    res.append(c)
                    c = ""
                if len(c) == 3:
                    res.append(c)
                    c = ""
                if len(c) == 4:
                    res.append(c[:2])
                    res.append(c[2:])
                    c = ""
            if len(c) == 0:
                break 
                
        return "-".join(res)
                    
                
    
   