class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        helper = defaultdict(int)
        for string in words:
            key = "".join(sorted(string[0::2])+sorted(string[1::2]))
            helper[key] += 1
        return len(helper)
     
