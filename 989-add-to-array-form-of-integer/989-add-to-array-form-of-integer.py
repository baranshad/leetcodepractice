class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if len(num) < len(str(k)):
            for i in range(len(str(k))- len(num)):
                num.insert(0,0)
                
        res = ""
        carry = 0
        for i in range(len(num)-1, -1, -1):
            curval = 0
            val = (num[i] + k % 10 + carry) % 10 
            carry = (num[i] + k % 10 + carry) // 10 
            res += str(val)
            curval = val 
            k = k//10 
        if carry:
            res += "1"
        return list(res[::-1])
            