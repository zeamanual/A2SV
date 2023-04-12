class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols = len(image),len(image[0])
        visited = set()

        def is_valid(x,y):
            return x < rows and x >= 0 and y < cols and y >= 0

        def dfs(curr,original,new_col):
            nonlocal image
            visited.add((curr[0],curr[1]))
            if(image[curr[0]][curr[1]] != original):
                return
            
            image[curr[0]][curr[1]]= new_col
            for dir_cor in directions:
                new_x, new_y = curr[0]+dir_cor[0],curr[1]+dir_cor[1]
                if(is_valid(new_x,new_y) and (new_x, new_y) not in visited):
                    dfs((new_x,new_y),original,new_col)

        dfs((sr,sc),image[sr][sc],color)
        return image
