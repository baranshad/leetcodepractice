class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = int(len(sequence)/len(word))
        print(n)
        for i in range(n,0,-1):
            if word*i in sequence:
                return i 
        else:
            return 0
        
    
    #for i in range(len(sequence)//len(word)+1,0,-1):
            #if i*word in sequence:
                #return i
        #else:
            #return 0