class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def helper(word, i):
            if word[0] in ["a","e","i","o","u", "A", "E", "I", "O", "U"]:
                word = word + "ma" + "a"*(i)
            else:
                word = word[1:] + word[0] + "ma" + "a"*(i)
            return word 
        
        buffer = []
        res = ""
        count = 0 
        for i, char in enumerate(sentence):
            if char.isalnum():
                buffer.append(char)
                if i != len(sentence)-1:
                    continue 
            if len(buffer) > 0:
                count += 1 
                word = "".join(buffer)
                res += helper(word, count) + " "
            buffer = []
        
        return res[:-1]
            