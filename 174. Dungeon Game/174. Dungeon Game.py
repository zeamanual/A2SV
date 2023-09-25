class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        @lru_cache(None)
        def helper(row,col):
            # print(row,col)
            if(row>=len(dungeon) or col>=len(dungeon[0])):
                return float('inf')
                
            if(row==len(dungeon)-1 and col == len(dungeon[0])-1):

                return -dungeon[row][col]
            else:
                return -dungeon[row][col] + min( max(0, helper(row+1,col)),max(0,helper(row,col+1)))

        # print(helper(0,0))
        return max(1,helper(0,0)+1)
