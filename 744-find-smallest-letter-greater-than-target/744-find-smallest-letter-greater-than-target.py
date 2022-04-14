class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ## special case for "z" 
        if target >= letters[-1]:
            return letters[0]
        l = 0
        r = len(letters) -1 
        while l<= r:
            m = l + (r-l)//2 
            if letters[m] <= target:
                l = m+1 
                
            if letters[m] > target:
                r = m -1 
                
        return letters[l]
        
