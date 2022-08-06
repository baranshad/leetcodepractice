class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        arr_sort= sorted(arr)
        rank = 1 
        for i in arr_sort:
            if i in d:
                continue
            else:
                d[i] = rank 
                rank = rank +1 
        #print(d)
        return [d[i] for i in arr]