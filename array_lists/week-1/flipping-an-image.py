class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
     
        for row in image:
             
            row.reverse()
             
            row[:] = [1 - value for value in row]
        
        return image