class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversed = []
        while matrix:
            # top
            traversed += matrix.pop(0) 
            # right
            traversed += [row.pop() for row in matrix] 
            if not matrix or not matrix[0]: break
            # bottom
            traversed += matrix.pop()[::-1]
            # left
            traversed += [row.pop(0) for row in matrix][::-1] 
            if not matrix or not matrix[0]: break
        return traversed
