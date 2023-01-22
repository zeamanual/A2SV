class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic_squares = 0
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                magic_squares += self.is_magic_square(grid,row, col)
        return magic_squares
    def is_magic_square(sellf,grid,row, col):
        nums = set(range(1, 10))
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if grid[r][c] in nums:
                    nums.remove(grid[r][c])
                else:
                    return False
        sum1 = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
        sum2 = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]
        if sum1 != sum2:
            return False
        for r in range(row - 1, row + 2):
            if grid[r][col - 1] + grid[r][col] + grid[r][col + 1] != sum2:
                return False
        for c in range(col - 1, col + 2):
            if grid[row - 1][c] + grid[row][c] + grid[row + 1][c] != sum2:
                return False
        return True
