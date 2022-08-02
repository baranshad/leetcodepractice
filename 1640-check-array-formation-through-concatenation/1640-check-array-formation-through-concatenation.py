class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        i = 0
        mapping = {d[0]: d for d in pieces}
        while i < n:
            if arr[i] not in mapping:
                return False 
            else:
                for x in mapping[arr[i]]:
                    if x != arr[i]:
                        return False 
                    i += 1 
        return True 