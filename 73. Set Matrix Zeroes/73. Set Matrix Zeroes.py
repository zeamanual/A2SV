class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeros_loc=set()

        for row in range(rows):
            for col in range(cols):
                if(matrix[row][col]==0):
                    zeros_loc.add((row,col))

        for row,col in zeros_loc:
            # setting the columns zero
            for i in range(rows):
                matrix[i][col]=0

            # setting the row zero
            for j in range(cols):
                matrix[row][j]=0
