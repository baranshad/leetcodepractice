class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set() 
        for word in emails:
            name, domain = word.split('@')
            local = name.split('+')[0].replace('.','')
            res.add(local+'@'+domain)
            
        return len(res)
                