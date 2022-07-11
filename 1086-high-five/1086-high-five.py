class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in items:
            d[i[0]].append(i[1])
        
        res = [int(sum(sorted(j, reverse=True)[:5])/5) for j in d.values()]
        ids = [i for i in d.keys()]
        ans = [[ids[i],res[i]] for i in range(len(ids))]
        return sorted(ans) 