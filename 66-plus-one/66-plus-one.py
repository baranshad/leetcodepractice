class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n-1
        while i >= 0: 
            if digits[i] == 9:
                digits[i] = 0 
            else:
                digits[i] = digits[i]+1 
                return digits
                break 
            i = i- 1 
                
        return [1]+ digits 