class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l = list(word)
        for i, val in enumerate(l):
            if val.isalpha():
                l[i] = str(" ")
        res = "".join(l).split()
        ans = set([int(i) for i in res])
        #print(ans)
        return len(ans)