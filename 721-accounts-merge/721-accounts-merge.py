class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = {}
        email_to_name = {}
        
        def find(x):
            # build a new node if not in uf
            if x not in uf:
                uf[x] = x
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
            
        for name, *emails in accounts:
            if len(emails) == 1:
                # build a new node if not in uf
                # path compress if already in uf
                find(emails[0])

            for e1, e2 in itertools.combinations(emails, 2):
                # it is redundant to uniuon each combination
                # but considering that path compress is done alone with union
                # it is worthy by making further find() to be O(1) in time cost
                union(e1, e2)
                
            for email in emails:
                if email not in email_to_name:
                    email_to_name[email] = name
        
        group_by_root = collections.defaultdict(list)
        for email in uf:
            group_by_root[find(email)].append(email)
            
        print(group_by_root, email_to_name)
        
        return [[email_to_name[root]] + sorted(emails) for root, emails in group_by_root.items()]