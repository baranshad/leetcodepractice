class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        letters = sum(c.isalpha() for c in s)
        digits = n - letters
        if abs(letters - digits) > 1:
            return ''
        
        res = [''] * n
        i = 0 if letters >= digits else 1
        j = 1 - i
        
        for c in s:
            if c.isalpha():
                res[i] = c
                i += 2
            else:
                res[j] = c
                j += 2
        
        return ''.join(res)

        