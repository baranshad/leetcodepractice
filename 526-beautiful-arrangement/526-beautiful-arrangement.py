class Solution:
    def countArrangement(self, n: int) -> int:
        def divisiable(n,k):
            return n % k == 0 or k % n == 0 
        
        res = 0 
        def helper(idx, stack):
            nonlocal res 

            if len(stack) == n:
                res += 1 
                return 
            
            for i in range(1, n+1):
                if i not in stack and divisiable(i,idx):
                    stack.append(i)
                    helper(idx+1, stack)
                    stack.pop()
        helper(1,[])
        return res
    
    
    