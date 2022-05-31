class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for j in range(len(digits)-1, -1, -1):
            if digits[j] == 9:
                digits[j] = 0
            else:
                digits[j] += 1 
                break
                print(digits)
        
        if digits[0] != 0:
            return digits

        elif digits[0] == 0:
            return [1] + digits
        
        
        
## case when digits[-1] < 9
## digits[-1] = digits[-1]+1 
## case when digits[-1] == 9 
## go down from -2  to 0 
### 3099
## if < 9   +1 
## else  == 9  0 and move next 
## if j == 0 then 
