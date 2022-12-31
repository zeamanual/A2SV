class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_size = len(grid)
        column_size = len(grid[0])
        row_zero_sum=[]

        # calculating zero's count of each row
        for i in range(row_size):
            zero_sum=0
            for j in range(column_size):
                if(grid[i][j]==0):
                    zero_sum+=1
            row_zero_sum.append(zero_sum)

        column_zero_sum=[]

        # calculating one's count of each column
        for j in range(column_size):
            zero_sum=0
            for i in range(row_size):
                if(grid[i][j]==0):
                    zero_sum+=1
            column_zero_sum.append(zero_sum)

        diff=[[ 0 for _ in range(column_size)] for _ in range(row_size)]

        # computing the difference matrix
        for i in range(row_size):

            for j in range(column_size):
                row_one_sum = column_size-row_zero_sum[i]
                col_one_sum = row_size- column_zero_sum[j]
                diff[i][j] = row_one_sum + col_one_sum - row_zero_sum[i] - column_zero_sum[j] 

        return diff





