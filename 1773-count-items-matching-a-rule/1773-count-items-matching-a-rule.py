class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        # Edge Case: ruleKey is neither of the required strings.
		# In such a case, this block of code prevents the for-loop from running needlessly, thus reducing runtime and memory uptake.
        #if ruleKey not in ['type', 'color', 'name']:
            #return count
        
        for i in items:
            if ruleKey == 'type' and i[0] == ruleValue:
                    count += 1
            elif ruleKey == 'color' and i[1] == ruleValue:
                    count += 1
            elif ruleKey == 'name' and i[2] == ruleValue:
                    count += 1
        
        return count