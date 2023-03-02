class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        row_size = len(grid[0])
        row1_psum = grid[0]
        row2_psum = grid[1]

        # calculating prefix sum 
        for index in range(1,row_size):
            row1_psum[index]+=row1_psum[index-1]
            row2_psum[index]+=row2_psum[index-1]

        max2=float('inf')
        # checking all posibilities 
        for index in range(row_size):

            choice1 = row1_psum[row_size-1]-row1_psum[index]
            choice2 = row2_psum[index-1] if index>0 else 0

            curr_max = max(choice1,choice2)
            max2= min(curr_max,max2)

        return max2
