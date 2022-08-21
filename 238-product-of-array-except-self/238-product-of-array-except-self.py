class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product1 = [1]
        temp  =  1
        for i in range(len(nums)-1):
            temp = nums[i]*temp 
            product1.append(temp)
            
        nums2 = nums[::-1]    
        product2 = [1]
        temp2  =  1
        for i in range(len(nums2)-1):
            temp2 = nums2[i]*temp2 
            product2.append(temp2)
            
        return [product1[i]*product2[len(product2)-1-i] for i in range(len(product1))]