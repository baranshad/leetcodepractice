class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        memo = [0]*len(calories)
        memo[0] = sum(calories[0:k])
        if memo[0] < lower:
            points -= 1
        if memo[0] > upper:
            points += 1
        for i in range(1,len(calories)-k+1):
            memo[i] =  memo[i-1] + calories[i+k-1] - calories[i-1]
            if memo[i] < lower:
                points -= 1
            if memo[i] > upper:
                points += 1
            #print(i,memo,points)
        return points
   