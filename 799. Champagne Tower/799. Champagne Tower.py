class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        answer = [[0 for i in range(101)] for j in range(101)]
        if(poured<1):
            return 0
        
        answer[0][0] = poured        
        for i in range(100):
            for j in range(100):

                curr = answer[i][j]
                if(curr<=1):
                    continue
                else:
                    print(i,j,'cords')
                    answer[i][j]=1
                    over_flow = (curr-1)/2
                    answer[i+1][j]+=over_flow
                    answer[i+1][j+1]+=over_flow

        return answer[query_row][query_glass]
