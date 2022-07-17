class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        lennums = [len(list(str(i))) for i in nums]
        return len([j for j in lennums if j%2==0])