class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minv = float("inf")
        ans = []
        
        for i in range(len(arr)-1):
            curff = arr[i+1] - arr[i]
            
            if curff < minv:
                ans = [[arr[i], arr[i+1]]]
                minv = curff 
            elif curff == minv:
                ans.append([arr[i], arr[i+1]])
        return ans 