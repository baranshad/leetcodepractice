class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        for i,j in zip([lower-1, *nums], [*nums, upper+1]):
            print(i,j)
            if j - i == 2:
                ans.append(str(i+1))
            elif j - i >2:
                ans.append(str(i+1) + "->" + str(j-1))
        return ans 