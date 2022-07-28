class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1= len(nums1)
        m2 = len(nums2)
        
        arr = []
        c2 = Counter(nums2)
        c1 = Counter(nums1)
        if m1 <= m2:
            for i in nums1:
                if i in c2 and c2[i] > 0 :
                    arr.append(i)
                    c2[i] -= 1 
                    
        else:
            for i in nums2:
                if i in c1 and c1[i] > 0 :
                    arr.append(i)
                    c1[i] -= 1 
        
        return arr
            