class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        rows=len(grid)
        cols=len(grid[0])

        largest_matr=[ [1 for j in range(cols-2)] for i in range(rows-2) ]

        for i in range(1,rows-1):
            for j in range(1,cols-1):

                max_num=1
                for row in range(i-1,(i-1)+3):
                    for col in range(j-1,(j-1)+3):
                        max_num=max(max_num,grid[row][col])

                largest_matr[i-1][j-1]=max_num

        return largest_matr



        
