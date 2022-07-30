class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = ''.join(s.split('-')).upper()[::-1]
        print(s)
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i+k])
            
        return '-'.join(res)[::-1]