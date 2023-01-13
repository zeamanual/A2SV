class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows-1
        current_row=(start+end)//2

        while(start<=end):
            if(matrix[current_row][0]>target):
                end=current_row-1
                current_row=(start+end)//2

            elif(matrix[current_row][0]<target):
                # current_row+=1
                for col_index in range(cols):
                    print(col_index,matrix[current_row][col_index])
                    if(matrix[current_row][col_index]==target):
                        return True
                start=current_row+1
                current_row=(start+end)//2

            else:
                return True

        return False




