class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return 0 
        
        ans  =  []
        word_freq = {}
        i = 0
        j = 0 
        while j < len(nums):
            if nums[j] not in word_freq:
                word_freq[nums[j]] = 0
            word_freq[nums[j]] += 1    
            
            if j-i+1 == k:
                ans.append(len(word_freq))
                word_freq[nums[i]] -= 1 
                if word_freq[nums[i]] == 0:
                    del word_freq[nums[i]]
                i += 1 
            j+= 1 
        return ans 