class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for row in matrix:
            for num in row:
                temp.append(num)
        heapq.heapify(temp)
        i = 0
        while(i<k):
            poped = heapq.heappop(temp)
            i+=1

        return poped
