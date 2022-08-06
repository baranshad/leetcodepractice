class Solution:
    def modifyString(self, s: str) -> str:
        ans = list(s)
        use3 = ["a","b","c"]
        for i, char in enumerate(ans):
            if char == "?":
                temp = set()
                if i != 0:
                    temp.add(ans[i-1])
                if i != len(s)-1:
                    temp.add(ans[i+1])
                ans[i] = (set(use3)- temp).pop()
                
        return "".join(ans) 
   
       