class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        num_set = set(nums)
        for i in range(1, len(nums)+1):
            if( i not in num_set ):
                return i

        return len(nums)+1
