class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        
        def computeIndex(square):
            r, c = divmod(square-1, n)
            if r % 2 ==0:
                return n-1-r, c 
            else:
                return n-1-r, n-1-c 
            
            
        visited = set()
        q = deque([])
        q.append((1,0))
        while q:
            cur_square, step_num = q.popleft()
            r, c = computeIndex(cur_square)
            if board[r][c]!= -1:
                cur_square = board[r][c]
                
            if cur_square == n*n:
                return step_num 
            
            for new_square in range(cur_square+1, min(cur_square+6, n*n) + 1):
                if new_square not in visited:
                    visited.add(new_square)
                    q.append((new_square, step_num+1))
                    
        return -1 