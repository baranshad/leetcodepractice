class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(li, l, r):
            while l< r:
                li[l], li[r] = li[r], li[l]
                l += 1 
                r -= 1 
       
        reverse(s, 0, len(s)-1)
        l = 0 
        for i, c in enumerate(s):
            if c == " ":
                reverse(s,l, i-1)
                l = i + 1 
 
        reverse(s,l, len(s)-1 )
        print(s)
        