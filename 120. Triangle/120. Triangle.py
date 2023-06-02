class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @lru_cache(None)
        def get_min(row,col):
            if(row>=len(triangle)):
                return 0
            curr_cost = triangle[row][col]
            option1 = get_min(row+1,col)
            option2 = get_min(row+1,col+1)


            return min(curr_cost+option1,curr_cost+option2)


        return get_min(0,0)
