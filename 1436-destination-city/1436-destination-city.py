class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        e = [j for (i, j) in paths]
        d = {}
        allpaths = []
        for i in range(len(paths)):
            allpaths.extend(paths[i])
        c = Counter(allpaths)
        for i, count in c.items():
            if count == 1 and i in e:
                return i 