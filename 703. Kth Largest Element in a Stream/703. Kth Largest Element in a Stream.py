class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while(len(nums)>k):
            heapq.heappop(nums)
        self.nums = nums        

    def add(self, val: int) -> int:

        heapq.heappush(self.nums,val)
        if(len(self.nums)==1 ):
            return val
        elif(len(self.nums)<=self.k):
            return self.nums[0]
            
        heapq.heappop(self.nums)

        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
