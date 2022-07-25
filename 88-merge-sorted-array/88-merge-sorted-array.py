class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1 = nums1[:m]
        i = j = 0 
        for k in range(m+n):
            if j >= n or (i<m and m1[i] <= nums2[j]):
                nums1[k]= m1[i]
                i+=1 
            else:
                nums1[k] = nums2[j]
                j+=1 
                
                
    