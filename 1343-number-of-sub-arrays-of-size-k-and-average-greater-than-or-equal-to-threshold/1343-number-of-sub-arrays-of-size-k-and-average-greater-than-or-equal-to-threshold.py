class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sums = [0]*(len(arr)+1)
        for i in range(1, len(arr)+1):
            sums[i] = sums[i-1] + arr[i-1]
 
        ans = 0    
        for j in range(len(arr), k-1, -1):
            print(j, j-k)
            if sums[j] - sums[j-k] >= k*threshold:
                ans+= 1 
        return ans 