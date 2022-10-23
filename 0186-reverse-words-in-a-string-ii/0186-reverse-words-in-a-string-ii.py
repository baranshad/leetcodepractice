class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            while l< r:
                s[l], s[r] = s[r], s[l]
                l += 1 
                r -= 1 
        n = len(s)-1
        reverse(0, n)
        l = 0 
        for i, c in enumerate(s):
            if c == " ":
                reverse(l, i-1)
                l = i + 1 
 
        reverse(l, n)

        