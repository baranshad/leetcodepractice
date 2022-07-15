class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        
        if s == goal:
            seen = set()
            for i in s:
                if i in seen:
                    return True 
                seen.add(i)
            return False 
        
        else:
            pairs = []
            for i, j in zip(s, goal):
                if i != j:
                    pairs.append((i,j))
                if len(pairs) >= 3: return False 
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]