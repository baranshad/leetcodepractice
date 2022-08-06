class Solution:
    def maximumTime(self, time: str) -> str:
        ans = list(time)
        for i in range(len(ans)):
            if ans[i] == "?":
                if i==0:
                    if ans[i+1] in ['0', '1', '2', '3', '?']:
                        ans[i] = '2' 
                    else:
                        ans[i] = '1'
                elif i ==1:
                    if ans[i-1] in ['1','0']:
                        ans[i] ='9'
                    else:
                        ans[i] = '3'
                elif i==3:
                    ans[i] = '5'
                elif i==4:
                    ans[i] = '9'
  
        return ''.join(ans)