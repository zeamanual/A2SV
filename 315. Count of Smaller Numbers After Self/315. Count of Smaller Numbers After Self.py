from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        answer = [0]*len(nums)
        sorted_list = SortedList([])

        
        for index in range(len(nums)-1,-1,-1):

            answer[index]=bisect_left(sorted_list,nums[index])

            sorted_list.add(nums[index])

        return answer
        
