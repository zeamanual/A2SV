class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        checked = set()
        curr = []
        self.max_so_far=nums[0]
        self.count = 0
        self.backtrack_or(nums,0,checked,[])

        return self.count


    def backtrack_or( self, nums, index, checked,curr):
        if(len(curr)>0):
            curr_val = self.check_max_or(curr)
            if(curr_val==self.max_so_far):
                self.count+=1
            elif(curr_val > self.max_so_far ) :
                self.max_so_far = curr_val
                self.count = 1

        for i in range(index, len(nums)):
            if(i in checked):
                continue
            checked.add(i)
            curr.append(nums[i])
            self.backtrack_or(nums,i+1, checked,curr)
            curr.pop()
            checked.discard(i)

    def check_max_or(self,arr):
        curr= arr[0]
        for num in arr:
            curr = curr | num

        return curr
