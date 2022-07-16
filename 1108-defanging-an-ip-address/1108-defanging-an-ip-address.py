class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i.isalnum():
                res += i 
            elif i == ".":
                res += "[.]"
                
        return res