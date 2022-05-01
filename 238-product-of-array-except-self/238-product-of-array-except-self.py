class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product1 = [1]
        product2 = []
        temp = 1
        for i in range(len(nums)-1):
            temp = nums[i] * temp 
            product1.append(temp)
        temp2 = 1   
        for j in range(len(nums)-1, 0, -1):
            temp2 = nums[j] * temp2
            product2.append(temp2)
        
        product2 = product2[::-1]
        product2.append(1)
        
        return [product1[i]*product2[i] for i in range(len(product1))]