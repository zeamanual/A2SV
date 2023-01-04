class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        row_size=len(mat)
        col_size=len(mat[0])

        diagonals={}

        for i in range(row_size):
            for j in range(col_size):
                indices_sum = i+j
                if(indices_sum in diagonals):
                    diagonals[indices_sum].append(mat[i][j])
                else:
                    diagonals[indices_sum]=[mat[i][j]]

        diagonals_list=[]
        for key,value in diagonals.items():
            if(key%2==0):
                diagonals_list.extend(reversed(value))
            else:
                diagonals_list.extend(value)

        return diagonals_list

        
