class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [ -num for num in piles]
        heapq.heapify(piles)
        i =0
        while(i<k):
            curr_max = -heapq.heappop(piles)
            curr_max -= floor(curr_max/2)
            heapq.heappush(piles,-curr_max)
            i+=1

        return -sum(piles)
