from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor =image[sr][sc]
        def changecolor(sr,sc):
            
            if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc] ==oldcolor and image[sr][sc] !=color :
                image[sr][sc] =color
            
                changecolor(sr-1,sc)
                changecolor(sr+1,sc)
                changecolor(sr,sc-1)
                changecolor(sr,sc+1)

            
        changecolor(sr,sc)
        return image
        
image = [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1
sc = 1
color = 2
s=Solution()
print(s.floodFill(image,sr,sc,color))

