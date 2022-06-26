class Solution:
    def numSquares(self, n: int) -> int:
        res = [float(inf)]*(n+1)
        res[0] = 0
        #print(int(sqrt(13)))
        squares = [i**2 for i in range(1, int(sqrt(n)+1))]
        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break 
                res[i] = min(res[i], res[i-square] + 1) 
        return res[-1]
            