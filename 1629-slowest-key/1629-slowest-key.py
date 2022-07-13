class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = [releaseTimes[0]]
        for i in range(len(releaseTimes)-1):
            res.append(releaseTimes[i+1]-releaseTimes[i])
        
        d= defaultdict(list)
        for i,val in enumerate(res):
            d[val].append(keysPressed[i])
                
        s_d = sorted(d.items(), key=lambda x:x[0], reverse=True)
        return (sorted(s_d[0][1],reverse=True)[0])