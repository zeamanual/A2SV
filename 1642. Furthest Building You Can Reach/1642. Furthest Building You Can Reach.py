class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []
        
        for i in range(len(heights)-1):
            curr_diff = heights[i+1]-heights[i]

            if(curr_diff>0):
                heapq.heappush(heap,curr_diff)

                if(ladders>0):
                    ladders-=1
                    continue
                else:
                    required_bricks = heapq.heappop(heap)

                    if(required_bricks<=bricks):
                        bricks-=required_bricks
                    else:
                        return i

        return len(heights)-1
