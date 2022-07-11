class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumall = sum(arr)
        if sumall % 3 != 0: 
            return False 
        partial = sumall // 3 
        n = len(arr)
        i = ans1 = 0
        while i < n:
            ans1 += arr[i]
            if ans1 == partial:
                break 
            i += 1 
        print(i)        
        if i >= n - 2: return False 
        ans2 = 0
        j = i + 1
        while j < n: 
            ans2 += arr[j]
            if ans2 == partial:
                break 
            j += 1 
        print(j)   
        if j >= n-1 : 
            return False 
        else:
            return True
        