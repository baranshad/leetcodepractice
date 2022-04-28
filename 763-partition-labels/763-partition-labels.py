class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict1 = {}
        for i in range(len(s)):
	        dict1[s[i]] = i
        ans=[]
        start = 0 
        end = 0
        for i in range(len(s)):
            end = max(dict1[s[i]], end)
            if end == i:
                ans.append(end-start+1)
                start = end+1
        return ans 
        