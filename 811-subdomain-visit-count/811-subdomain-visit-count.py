class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()
        for c in cpdomains:
            s = c.split()
            #d[s[-1]] = int(s[0])
            char_s = s[-1].split(".")
            for i in range(len(char_s)):
                ans['.'.join(char_s[i:])] += int(s[0])
                
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
