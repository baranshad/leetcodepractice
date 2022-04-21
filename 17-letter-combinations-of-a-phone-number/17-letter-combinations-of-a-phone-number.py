class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        def helper(idx, path):
            if len(path) == len(digits):
                ans.append("".join(path))   
                return 

            letters = d[digits[idx]]
            for i in letters:
                path.append(i)
                helper(idx+1, path)
                path.pop()
                
        helper(0, [])
        return ans 
                