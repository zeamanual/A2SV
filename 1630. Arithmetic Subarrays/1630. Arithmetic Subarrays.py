class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result =[]
        for index in range(len(l)):
            start_index = l[index]
            end_index = r[index]
            current_sub_array = nums[start_index:end_index+1]
            current_sub_array.sort()
            diffrence =None
            isArithemtic=True
            for sub_index in range(len(current_sub_array)-1):
                if(diffrence==None):
                    diffrence = current_sub_array[sub_index]-current_sub_array[sub_index+1]
                else:
                    if(diffrence !=(current_sub_array[sub_index]-current_sub_array[sub_index+1])):
                        isArithemtic=False
            result.append(isArithemtic)
        return result
