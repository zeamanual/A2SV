class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        equal_count=0
        rows = {}
        matrix_size = len(grid)

        for row_index in range(matrix_size):
            row_str=[]
            for col_index in range(matrix_size):
                row_str.append(str(grid[row_index][col_index])+',')

            rows[row_index]={''.join(row_str):1}

        for col_index in range(matrix_size):
            current_col=[]
            for row_count in range(matrix_size):
                current_col.append(str(grid[row_count][col_index])+',')
                
            current_col=''.join(current_col)

            for row_index in range(matrix_size):
                if(rows[row_index].get(current_col,0)==1):
                    equal_count+=1
            
        return equal_count
                
