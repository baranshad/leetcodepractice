class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0 
        temp = 0
        for i in gain:
            ans += i
            temp = max(ans, temp)
        return temp 
         