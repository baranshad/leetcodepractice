class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for j in range(n-1, -1, -1):
            if digits[j] == 9:
                digits[j] = 0 
            else:
                digits[j] = digits[j] + 1 
                return digits 
                break 
        return [1] + digits
    
    