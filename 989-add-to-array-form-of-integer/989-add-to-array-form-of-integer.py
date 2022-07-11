class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numint = "".join(str(i) for i in num)
        res = int(numint) + k 
        ans = [int(i) for i in str(res)]
        return ans 