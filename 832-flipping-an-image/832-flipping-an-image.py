class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        onem = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1-image[i][j])
            onem.append(temp[::-1])
        return onem