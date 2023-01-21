class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # first reversing the matrix from top to bottom

        rows = len(matrix)
        cols  = len(matrix[0])

        for row in range(rows//2):
            for col in range(cols):
                matrix[row][col],matrix[(rows-1)-row][col]=matrix[(rows-1)-row][col],matrix[row][col]

        for row in range(rows):
            for col in range(cols):
                if(row>col):
                    matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]

        return matrix
