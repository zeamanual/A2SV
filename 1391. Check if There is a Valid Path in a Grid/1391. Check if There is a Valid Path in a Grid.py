class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        neighbour_details = {
            1:[(0,-1),(0,1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }

        row,col = len(grid),len(grid[0])
        visited = [ [0 for i in range(col)] for j in range(row) ]
        
        def in_bound(r,c):
            if(r < row and r >= 0 and c < col and c >= 0):
                return True
            return False

        is_possible = False
        def dfs(cur_row,cur_col):
            nonlocal is_possible

            if( cur_row == row-1 and cur_col == col-1):
                is_possible = True
                return True
            
            for row_shift,col_shift in  neighbour_details[grid[cur_row][cur_col]]:
                
                
                new_row, new_col = cur_row + row_shift, cur_col + col_shift
                is_neighbour = in_bound(new_row,new_col) and (- row_shift,- col_shift) in neighbour_details[grid[new_row][new_col]] 


                if( is_neighbour and not visited[new_row][new_col]):
                    visited[new_row][new_col]=1
                    if( dfs(new_row,new_col) ):
                        return True

            return False

        visited[0][0]=1
        dfs(0,0)
        return is_possible
