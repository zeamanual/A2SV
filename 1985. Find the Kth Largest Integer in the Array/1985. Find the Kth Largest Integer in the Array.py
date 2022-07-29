class Solution(object):
    def kthLargestNumber(self, nums, k):
        sorted_nums = sorted(nums,key=lambda num:int(num))
        return sorted_nums[-k]
        
