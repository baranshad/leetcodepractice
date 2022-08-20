class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1 
        
        res = [gas[i]-cost[i] for i in range(len(gas))]
        ans = 0
        start = tank = 0
        for i in range(len(res)):
            tank += res[i]
            if tank < 0:
                start = i + 1 
                tank = 0
        return start 