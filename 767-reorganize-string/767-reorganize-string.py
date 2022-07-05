class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = {}
        for i in s:
            if i in s_counter:
                s_counter[i] += 1 
            else:
                s_counter[i] = 1 

        
        #for i,j in s_counter.items():
            #print(i,j)
        ans = ["w"] 
        characterWithMaxFrequency = ''
        maxFrequency = 0
        for i in range(len(s)):
            #find char with max frequency
            for char, frequency in s_counter.items():
                if frequency > maxFrequency and char != ans[-1]:
                    characterWithMaxFrequency = char
                    maxFrequency = frequency
            ## not equal ans[-1]
            if characterWithMaxFrequency == '': return ""
            print(characterWithMaxFrequency)
            s_counter[characterWithMaxFrequency] = s_counter[characterWithMaxFrequency] - 1
            ans.append(characterWithMaxFrequency)
            maxFrequency = 0
            characterWithMaxFrequency = ''
            
        #temp = 
        return "".join(ans[1:])


        