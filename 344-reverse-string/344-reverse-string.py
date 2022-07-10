class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        init=0
        fin=len(s)-1
        while(init < fin):
            tmp=s[init]
            s[init]=s[fin]
            s[fin]=tmp
            init+=1
            fin-=1