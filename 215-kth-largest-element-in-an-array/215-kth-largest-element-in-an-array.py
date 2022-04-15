class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in range(k):
            minHeap.append(nums[i])
            
        for i in range(k, len(nums)):
            minHeap.sort()

            if (minHeap[0] > nums[i]):
                continue
        
            else:
                minHeap.pop(0)
                minHeap.append(nums[i])
        #print(sorted(minHeap))        
        return sorted(minHeap)[0]

                
 
        