class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        while i+1 < n and arr[i+1] > arr[i]:
            i += 1 
        
        
        if i == 0 or i == n-1:
            return False 
        
       
        
        for j in range(i, n-1):
            if arr[j+1] >= arr[j]:
                return False 
        return True