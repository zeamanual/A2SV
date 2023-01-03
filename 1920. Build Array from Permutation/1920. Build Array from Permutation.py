class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        arr = []
        nums_len = len(nums)
        for index in range(nums_len):
            arr.append(nums[nums[index]])

        return arr
