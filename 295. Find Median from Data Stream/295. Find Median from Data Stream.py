class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
           
        max_num  =heapq.heappop(self.min_heap) if(len(self.min_heap))>0 else float('inf')
        if(max_num!=float('inf')):
            heapq.heappush(self.min_heap,max_num)
        min_num = -heapq.heappop(self.max_heap) if(len(self.max_heap))>0 else float('-inf')
        if(min_num!=float('-inf')):
            heapq.heappush(self.max_heap,-min_num)

        if(len(self.min_heap)>len(self.max_heap)):
            poped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-poped)
        elif(len(self.max_heap)>1+len(self.min_heap)  ):
            poped = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,poped)
        elif( min_num>max_num):
            poped = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,poped)
            poped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-poped)
        

    def findMedian(self) -> float:
        if( (len(self.min_heap)+len(self.max_heap)) %2==0):

            poped1 = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap,poped1)
            
            poped2 = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap,-poped2)
            return (poped1+poped2)/2
        else:
            poped1 = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap,-poped1)
            return poped1

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
