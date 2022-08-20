class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()[::-1]
        ans = []
        for i in range(0,len(s), k):
            ans.append(s[i:i+k])
        res = '-'.join(ans)
        return res[::-1]
        
        #s = ''.join(s.split('-')).upper()[::-1]
        #res = []
        #for i in range(0, len(s), k):
            #res.append(s[i:i+k])
        #return "-".join(res)[::-1]