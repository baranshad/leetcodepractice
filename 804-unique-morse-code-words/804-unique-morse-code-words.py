class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            temp = ""
            for j in word:
                temp+= "".join(m[ord(j)-ord("a")])
            seen.add(temp)
        return len(seen)