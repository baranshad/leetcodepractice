class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = [str(sorted(i)) for i in dominoes]
        count = 0 
        for j in Counter(res).values():
            count += j*(j-1) //2
        return count 
    
    