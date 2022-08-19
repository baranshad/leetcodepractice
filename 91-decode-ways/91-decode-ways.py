class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def helper(index, s):
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s)-1:
                return 1
        
            answer = helper(index + 1, s)
            if int(s[index : index + 2]) <= 26:
                answer += helper(index + 2, s)

            return answer
        
        
        return helper(0, s)
        
        