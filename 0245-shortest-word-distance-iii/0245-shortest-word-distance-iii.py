class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx = 0 
        cur_word = None 
        min_dist = len(wordsDict)
        
        for i, w in enumerate(wordsDict):
            if w not in (word1, word2):
                continue 
            elif cur_word and w in (word1, word2) and (word1 == word2 or w != cur_word):
                min_dist = min(min_dist, i-idx)
                
            cur_word, idx = w, i 
            
        return min_dist 
                    
        