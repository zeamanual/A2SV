class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,columns = len(matrix),len(matrix[0])
        self.prefixSummedMatrix = [[0 for i in range(columns)] for i in range(rows)]
        for row in range(rows):
            sum = 0
            for column in range(columns):
                sum+=matrix[row][column]
                self.prefixSummedMatrix[row][column]=sum

        for column in range(columns):
            sum = 0
            for row in range(rows):
                sum+=self.prefixSummedMatrix[row][column]
                self.prefixSummedMatrix[row][column]=sum
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefixSummedMatrix[row2][col1-1] if col1>0 else 0
        top= self.prefixSummedMatrix[row1-1][col2] if row1>0 else 0
        topLeft= self.prefixSummedMatrix[row1-1][col1-1] if (row1>0 and col1 >0) else 0
        bottomRight = self.prefixSummedMatrix[row2][col2]
        result = bottomRight-left-top+topLeft

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
