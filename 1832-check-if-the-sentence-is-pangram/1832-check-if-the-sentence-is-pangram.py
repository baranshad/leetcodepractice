class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #d = [chr(ord("a")+i) for i in range(26)]
        list_s = list(sentence)
        sets = set(list_s)
        return len(sets) == 26
        