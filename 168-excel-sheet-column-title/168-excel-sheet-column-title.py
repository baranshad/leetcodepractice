class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        temp = ""
        while columnNumber > 0:
            val = (columnNumber-1) //26 
            
            remainder = (columnNumber-1) % 26 
            temp += chr(65 + remainder)
            columnNumber = val 
        return temp[::-1]
            
            
            
         #   ans = []
       # while columnNumber > 0:
            #ans.append(chr(65 + (columnNumber - 1) % 26))
           # columnNumber = (columnNumber - 1) // 26
       # return "".join(reversed(ans))
            