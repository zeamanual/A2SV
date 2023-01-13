class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows=len(mat)
        cols = len(mat[0])
        if( (rows*cols)!=(r*c)):
            return mat

        reshaped=[[0 for j in range(c)] for i in range(r)]
        
        for i in range(rows):
            for j in range(cols):
                unique_id=( ( i * cols ) + j )
                target_row=unique_id // c
                target_col = unique_id%c
                reshaped[target_row][target_col]=mat[i][j]

        return reshaped
