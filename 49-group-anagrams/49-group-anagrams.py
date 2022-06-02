class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def helper(s1):
            s1_list = sorted(list(s1)) 
            return ''.join(s1_list)

        d = {}
        for i in strs:
            
            if helper(i) in d:
                d[''.join(sorted(list(i)))].append(i)
            else:
                d[''.join(sorted(list(i)))] = [i]

        ans = [i for i in d.values()]
        return ans 
            
                