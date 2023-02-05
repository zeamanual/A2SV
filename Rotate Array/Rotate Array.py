class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        num_copy = nums.copy()
        total = len(nums)
        for i in range(total):
            final_index = self.get_index(i, k, total)
            nums[final_index] = num_copy[i]

    def get_index(self,current_index, shift, total):
        shift = shift % total
        result = current_index + shift
        if result <= total - 1:
            return result
        else:
            return result - total
