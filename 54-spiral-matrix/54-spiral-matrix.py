class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = up = 0 
        right = len(matrix[0]) -1 
        down = len(matrix) -1 
        
        res = []
        
        while len(res) < len(matrix[0]) * len(matrix):
            for col in range(left, right+1):
                res.append(matrix[up][col])
                
            for row in range(up+1, down+1):
                res.append(matrix[row][right])
                
            if up != down:
                for col in range(right-1, left-1, -1):
                    res.append(matrix[down][col])
                    
            if right != left:
                for row in range(down-1, up, -1):
                    res.append(matrix[row][up])
                    
            left += 1 
            right -= 1 
            up +=1 
            down -= 1 
        
        return res 
                