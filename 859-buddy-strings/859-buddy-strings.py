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
            res = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    res.append((s[i], goal[i]))
                if len(res) >= 3: return False 
            return len(res) == 2 and res[0] == res[1][::-1]
                    
                    