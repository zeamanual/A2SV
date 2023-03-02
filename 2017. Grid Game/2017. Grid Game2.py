class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        row_size = len(grid[0])

        # calculating prefix sum 
        for index in range(1,row_size):
            grid[0][index]+=grid[0][index-1]
            grid[1][index]+=grid[1][index-1]

        max2=float('inf')
        # checking all posibilities 
        for index in range(row_size):

            choice1 = grid[0][row_size-1]-grid[0][index]
            choice2 = grid[1][index-1] if index>0 else 0

            curr_max = max(choice1,choice2)
            max2= min(curr_max,max2)

        return max2
