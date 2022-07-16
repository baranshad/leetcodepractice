class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {"U": (0,-1), "D": (0,1), "R": (1,0), "L": (-1,0)}
        res = [0,0]
        for i in moves:
            res[0] = res[0] + d[i][0]
            res[1] = res[1] + d[i][1]
            print(res)
        return res == [0,0]