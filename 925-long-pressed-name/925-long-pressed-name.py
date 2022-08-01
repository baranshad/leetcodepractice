class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed) or name[0] != typed[0]:
            return False 
        
        i = 0 
        for j in typed:
            if i < len(name) and j == name[i]:
                i += 1 
            elif j != name[i-1]:
                return False 
        return i>= len(name)
                
            