class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: 
            return 0 
        
        for n in reversed(range(len(costs)-1)):
            costs[n][0] += min(costs[n+1][1], costs[n+1][2])
            costs[n][1] += min(costs[n+1][0], costs[n+1][2])
            costs[n][2] += min(costs[n+1][0], costs[n+1][1])
            
        return min(costs[0])