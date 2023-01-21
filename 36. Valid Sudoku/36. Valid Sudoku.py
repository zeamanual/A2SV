class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=9
        cols=9

        for row in range(rows):
            row_checked=False
            for col in range(cols):
                if(not row_checked):
                    row_checked=True
                    if(not self.checkRow(board,row)):
                        return False
                if(row<1):
                    if(not self.checkCol(board,col)):
                        return False
                if(row%3==0 and col%3==0):
                    if(not self.checkBox(board,row,col)):
                        return False       
        return True    

    
    def checkBox(self,board,start_row,start_col):
        visited=set()
        for row in range(start_row,start_row+3):
            for col in range(start_col,start_col+3):
                current_element = board[row][col]
                if(current_element not in visited and current_element!='.' ):
                    visited.add(current_element)
                elif(current_element!='.'):
                    return False    

        return True            


    def checkRow(self,board,target_row):
        visited=set()
        for element in board[target_row]:
            if(element not in visited and element!='.'):
                visited.add(element)
            elif(element!='.'):
                return False
        return True

    def checkCol(self,board,target_col):
        rows=len(board)
        visited=set()
        for row in range(rows):
            current_element = board[row][target_col]
            if(current_element not in visited and current_element !='.'):
                visited.add(current_element)
            elif(current_element!='.'):
                return False
        return True
