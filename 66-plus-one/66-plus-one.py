class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if set(digits) == {9}:
            digits = [1] + [0]* len(digits)
        else: 
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9: 
                    digits[i] = 0
                else:
                    digits[i] = digits[i]+1
                    break
                        
        return digits 
        