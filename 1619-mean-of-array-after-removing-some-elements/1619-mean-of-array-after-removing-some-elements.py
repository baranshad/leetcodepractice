class Solution:
    def trimMean(self, arr: List[int]) -> float:
        s = sorted(arr)
        nums = len(arr)//20
        #print(arr[nums-1: len(arr)-nums])
        return sum(s[nums: len(arr)-nums])/len(arr[nums: len(arr)-nums])
    
        #n = len(arr)
        #trim = n // 20
        #return sum(sorted(arr)[trim:n-trim]) / (n - 2*trim)