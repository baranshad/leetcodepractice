class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_count = text.split()
        lengh_word = len(word_count)
        spacecount = Counter(text)
        sc = spacecount[" "]
        
        if lengh_word == 1:
            return word_count[0] + " "*sc
        
        value = sc//(lengh_word-1)
        remainder = sc % (lengh_word-1)
        print(remainder)
        res = ""
        for i, word in enumerate(word_count):
            if i < lengh_word-1:
                res += word 
                res += " "*(value)
        res += word_count[-1]
        
        if remainder == 0:
            return res 
        elif remainder > 0:
            return res + " "*remainder 