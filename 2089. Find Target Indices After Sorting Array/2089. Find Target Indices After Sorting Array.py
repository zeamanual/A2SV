class Solution(object):
    def targetIndices(self, nums, target):
        size = len(nums)
        self.insertion_sort(nums)
        indices_list=[]
        for index in range(size):
            if(nums[index]==target):
                indices_list.append(index)
        return indices_list
    
    def insertion_sort(self,array):
        array_size = len(array)
        for index in range(1,array_size):
            temp_index=index
            while(array[temp_index]<array[temp_index-1] and temp_index > 0):
                array[temp_index],array[temp_index-1]=array[temp_index-1],array[temp_index]
            
