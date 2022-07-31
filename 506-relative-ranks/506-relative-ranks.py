class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dict_={}
        for i in score:
            dict_[i]=0
        c=len(score)
        heapify(score)
        
        while score:
            s = heappop(score)
            print(s)
            if c>3:
                dict_[s]=str(c)
            elif c==3:
                dict_[s]="Bronze Medal"
            elif c==2:
                dict_[s]="Silver Medal"
            else:
                dict_[s]="Gold Medal"
            c-=1
        return dict_.values()
         