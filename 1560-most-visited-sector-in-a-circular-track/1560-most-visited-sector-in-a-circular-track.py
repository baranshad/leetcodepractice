class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = defaultdict(int)
        
        for i in range(len(rounds)-1):
            if i == 0:
                cur = rounds[i] -1 
                counter[cur] +=1 
            while cur != rounds[i+1]-1:
                cur = (cur+1)%n 
                counter[cur] += 1 
        sc = [i+1 for i,j in counter.items() if j == max(counter.values())]
        return sorted(sc)
        
        