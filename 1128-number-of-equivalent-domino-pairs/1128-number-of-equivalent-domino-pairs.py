class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = [str(sorted(i)) for i in dominoes]
        count = 0 
        for i,j in Counter(res).items():
            if j > 1:
                count += j*(j-1)//2 
        return count 
    
    
    
    
    #d=dict()
        #for i in dominoes:
            #i.sort()            #Just to make everything equal and comparable
           # if(tuple(i) in d.keys()):   #In python, lists are unhashable so converted the list into tuples
            #    d[tuple(i)]+=1
            #else:
             #   d[tuple(i)]=1
        