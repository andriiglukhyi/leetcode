class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def traverse_grid(old, x, y, new):
            if x < 0 or y < 0 or x > len(image)-1 or y > len(image[0])-1 or image[x][y] == new:
                return
            image[x][y] = new
            traverse_grid(old, x+1, y, new)
            traverse_grid(old, x-1, y, new)
            traverse_grid(old, x, y+1, new)
            traverse_grid(old, x, y-1, new)
            
        traverse_grid(image[sr][sc], sr, sc, newColor)
        return image