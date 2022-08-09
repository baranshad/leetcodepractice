class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i in pieces:
            d[i[0]] = i 
            
        j = 0 
        while j < len(arr):
            if arr[j] not in d:
                return False 
            else:
                for x in d[arr[j]]:
                    if x!= arr[j]:
                        return False 
                    j += 1 
        return True 
                
            