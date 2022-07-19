class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        else:
            xs = list(str(x))
            return xs==xs[::-1]