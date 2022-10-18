class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        stack = [(0,1),(1,0),(0,-1),(-1,0)]
        m = [[0 for _ in range(n)] for x in range(n)]
        num = 2 
        turn = 1 
        side_step = 1 
        side_length = n
        i = j = 0
        m[0][0] = 1 
        while num <= n*n:
            if side_step == side_length:
                side_step = 0 
                stack.append(stack.pop(0))
                turn += 1 
                if turn ==2:
                    side_length -=1 
                    turn = 0 
            i += stack[0][0]
            j += stack[0][1]
            m[i][j] = num 
            num += 1 
            side_step += 1 
            
        return m 