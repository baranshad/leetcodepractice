class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        target_char = Counter(chars)
        ans = 0 
        def helper(w, d):
            for c in w:
                if c not in d or d[c]==0:
                    return 0 
                else:
                    d[c]-=1 
            return len(w)
        for w in words:
            ans += helper(w, target_char.copy())
            
        return ans  