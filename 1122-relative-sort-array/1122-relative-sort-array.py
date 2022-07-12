class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        print(d)
        notin= sorted([i for i in arr1 if i not in arr2])
        print(notin)
        res = []
        for i in arr2:
            res.extend([i]*d[i])
        res.extend(notin)
        return res 
    
    

        #for i in arr1:
           # lst[i]+=1   # just counting the occurence of each element and storing it in lst
        #for i in arr2:   
            #res.extend([i]*lst[i])   # adding to resultant list the element mutiplied by the number of times it appears using lst
        #diff=[]   
        #for i in arr1:
            #if i not in res:
                #diff.append(i)   #to find remaining elements of arr1 which are not in arr2
        #diff.sort() 
        #res.extend(diff)
       # return res