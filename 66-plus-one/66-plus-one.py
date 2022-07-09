class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] = digits[-1]+1 
        elif set(digits) == {9}:
            digits = [1] + [0]* len(digits)
        else: 
            if digits[-1] == 9:
                for i in range(len(digits)-1, -1, -1):
                    if digits[i] != 9: 
                        digits[i] = digits[i]+1 
                        break
                    else:
                        digits[i] = 0
                        
        return digits 
        