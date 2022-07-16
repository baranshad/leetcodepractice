class Solution:
    def removeVowels(self, s: str) -> str:
        d = ["a","e","i","o","u"]
        res = []
        for i in s:
            if i not in d:
                res.append(i)
        return "".join(res)