class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] ==0:
                leftempty = (i==0) or flowerbed[i-1] == 0
                rightempty = (i == len(flowerbed)-1) or flowerbed[i+1] == 0
                if leftempty and rightempty:
                    count += 1 
                    flowerbed[i] = 1 
        return count >= n