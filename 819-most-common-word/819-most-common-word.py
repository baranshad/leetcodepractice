class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        res = ""
        max_count = 0
        d = defaultdict(int)
        buffer = []
        banned_set = set(banned)
        for i, char in enumerate(paragraph):
            if char.isalnum():
                buffer.append(char.lower())
                if i != len(paragraph) -1 :
                    continue 
                    
            if len(buffer) > 0:
                word = "".join(buffer)
                if word not in banned_set:
                    d[word] +=1 
                    if d[word] > max_count:
                        max_count = d[word]
                        res = word 
            buffer = []
        return res 
                        
            