class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_c = Counter(sorted(words))
        words_sorted = sorted(words_c.items(), key= lambda x: x[1], reverse=True)
        res = [i for i, j in words_sorted][:k]
        return res 