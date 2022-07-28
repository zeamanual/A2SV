class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        new_list = []
        array_size = len(nums)
        
        for i in range(array_size):
            new_list.append(0)
        
        for current_num_index in range(array_size):
            for index in range(array_size):
                if(nums[index] < nums[current_num_index]):
                    new_list[current_num_index]+=1
        
        return new_list
        
