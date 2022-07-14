class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True 
        arr.sort()
        for i in range(1,len(arr)-1):
            if arr[i]- arr[i-1] != arr[i+1] - arr[i]:
                return False
        return True
    
    #arr.sort()
        #step = arr[1] - arr[0]
        #for i in range(len(arr)-1):
            #if arr[i+1] - arr[i] != step:
                #return False
        #return True