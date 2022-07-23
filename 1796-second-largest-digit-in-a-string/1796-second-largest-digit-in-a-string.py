class Solution:
    def secondHighest(self, s: str) -> int:
        digitset = set([int(i) for i in list(s) if i.isdigit()])
        digitset = sorted(list(digitset))
        print(digitset)
        if len(digitset) < 2:
            return -1 
        return digitset[-2]