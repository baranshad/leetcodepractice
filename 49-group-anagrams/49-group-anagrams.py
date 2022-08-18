class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def numconvert(word):
            numlist = [0]*26
            for i in word:
                numlist[ord(i)-ord('a')] += 1 
            return numlist 
        
        d = defaultdict(list)
        for i in strs:
            d[tuple(numconvert(i))].append(i)
            
        res = [j for i,j in d.items()]
        return res 
        
        