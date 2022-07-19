class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        elif n % 2 == 0:
            return "a"*(n-1) + "b"
        else:
            #print((n+1)/2, (n-1)/2)
            return "c" + "a" + "b"*(n-2)