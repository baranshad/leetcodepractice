class Solution:
    def grayCode(self, n: int) -> List[int]:
        temp = [0,1]
        i = 1 
        while i < n:
            new = temp[:]
            for j in new[::-1]:
                new.append(j + 2**i)
            temp = new 
            i+= 1 
            
        return temp 