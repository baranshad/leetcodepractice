class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        out = arr.copy()
        while True:
            i = 1 
            while i < len(arr)-1:
                if arr[i]<arr[i-1] and arr[i] < arr[i+1]:
                    out[i] += 1 
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    out[i] -= 1 
                i+=1 
            if out == arr:
                return arr 
            
            arr = out.copy()