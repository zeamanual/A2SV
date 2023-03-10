class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.curr_set = []
        self.answer = []
        self.size= len(nums)
        self.nums = nums
        self.helper(0)

        return self.answer

    def helper(self, index):
        if( index == self.size ):
            self.answer.append(self.curr_set.copy())
            return 

        self.curr_set.append(self.nums[index])
        self.helper(index+1)
        self.curr_set.pop()

        self.helper(index+1)
