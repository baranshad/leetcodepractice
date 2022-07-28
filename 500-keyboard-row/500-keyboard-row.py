class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set(list("qwertyuiop"))
        s2= set(list("asdfghjkl"))
        s3 = set(list("zxcvbnm"))
        ans = []
        for word in words:
            word_lower = word.lower()
            if set(list(word_lower)).issubset(s1) or set(list(word_lower)).issubset(s2) or set(list(word_lower)).issubset(s3):
                ans.append(word)
        return ans 