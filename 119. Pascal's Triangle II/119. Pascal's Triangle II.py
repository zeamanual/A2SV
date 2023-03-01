class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if(rowIndex==0):
            return [1]
        
        prev_row = self.getRow(rowIndex-1)
        curr_row = []
        for i in range(rowIndex+1):
            top_left = 0 if (i-1) < 0 else prev_row[i-1]
            top_right= 0 if (i == len(prev_row)) else prev_row[i]
            curr_row.append(top_left+top_right)

        return curr_row
