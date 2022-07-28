class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=len(nums)
        counter={}
        ans=[0,0]
        for i in nums:
            if i in counter:
                counter[i]+=1
                ans[0]=i
            else:
                counter[i]=1
        print(ans, counter)
        for i in range(l):
            print(i)
            if i+1 not in counter:
                ans[1] = i+1
                return ans
        
            
                