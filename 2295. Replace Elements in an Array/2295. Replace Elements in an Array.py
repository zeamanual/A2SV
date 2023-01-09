class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        num_index_dic = {}

        for index, num in enumerate(nums):
            num_index_dic[num]=index

        for operation_value in operations:
            nums[num_index_dic[operation_value[0]]]=operation_value[1]
            num_index_dic[operation_value[1]]=num_index_dic[operation_value[0]]
            del num_index_dic[operation_value[0]]

        return nums
