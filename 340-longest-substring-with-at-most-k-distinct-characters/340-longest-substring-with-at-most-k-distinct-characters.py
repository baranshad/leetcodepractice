class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        init, count = 0,0 
        visited = defaultdict(int)
        for i, val in enumerate(s):
            visited[val] = i
            while len(visited) > k: 
                if visited[s[init]] == init:
                    del visited[s[init]]
                init += 1 
            else:
                count = max(count, i-init+1)
        return count 