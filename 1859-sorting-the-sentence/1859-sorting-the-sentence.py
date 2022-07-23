class Solution:
    def sortSentence(self, s: str) -> str:
        s += " "
        ans = []
        temp = ""
        digitorder = []
        for i, val in enumerate(s):
            if val == " ":
                if len(temp) > 0:
                    ans.append(temp[:-1])
                    digitorder.append(temp[-1])
                    temp = ""
            elif val != " ":
                temp += val 
        d = {}
        for i, val in enumerate(digitorder):
            d[int(val)] = ans[i]
            
        sortedd = sorted(d.items(), key=lambda x: x[0])
        res = [j for i,j in sortedd]
        return " ".join(res)