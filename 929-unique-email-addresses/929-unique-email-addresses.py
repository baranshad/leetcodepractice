class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set() 
        for word in emails:
            temp = ""
            for i, char in enumerate(word):
                if char.isalpha():
                    temp += char 
                elif char == ".":
                    continue
                elif char =="+" or char == "@":
                    break 
                    
                    
            temp1 = ""
            for i, char in enumerate(reversed(word)):
                temp1 += char
                if char == "@":
                    break 
                    
            cur = temp + temp1[::-1]
            res.add(cur)
        return len(res)
                