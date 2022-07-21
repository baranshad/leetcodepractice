class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordlist= sentence.split()
        for i, word in enumerate(wordlist):
            if searchWord == word[:len(searchWord)]:
                return i+1
                break 
        return -1 
            
        