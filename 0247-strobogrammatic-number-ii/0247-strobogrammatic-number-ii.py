class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'], 
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        def helper(n,finallength):
            if n == 0:
                return [""]
            
            if n == 1:
                return ["0","1","8"]
            
            prev = helper(n-2,finallength)
            
            res = []
            for eachprev in prev:
                for i,j in reversible_pairs:
                    if i != "0" or n != finallength:
                        res.append(i + eachprev + j) 
                        
            return res 
        
        return helper(n, n)