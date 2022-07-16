class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for w in emails:
            temp = ""
            for j, c in enumerate(w):
                if c.isalpha():
                    temp+=c
                elif c == ".":
                    continue 
                elif c == "+" or c=="@":
                    break 
                    
            temp2 = ""
            for char in reversed(w):
                temp2 += char
                if char == "@":
                    break 
                    
            unique.add(temp+temp2[::-1])
            
        return len(unique)
                