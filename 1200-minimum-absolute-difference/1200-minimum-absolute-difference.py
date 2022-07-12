class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minv = float("inf")
        ans = []
        
        for i in range(len(arr)-1):
            curdiff = arr[i+1] - arr[i]
            if minv == curdiff:
                ans.append([arr[i], arr[i+1]])
            elif curdiff < minv:
                ans = [[arr[i], arr[i+1]]]
                minv = curdiff 
                
        return ans 