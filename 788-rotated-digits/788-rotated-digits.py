class Solution:
    def rotatedDigits(self, n: int) -> int:
        d = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
        ans = 0
        for i in range(1, n+1):
            s = str(i)
            temp =""
            for j in s:
                if j in d:
                    temp += d[j]
                else:
                    temp = ""
                    break
            
            if temp and int(temp) != i:
                ans += 1 
        return ans 