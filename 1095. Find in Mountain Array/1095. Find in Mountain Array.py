# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def get_peak():
            left = 1
            right = mountain_arr.length()-2
        
            while(left<right):
                mid = (left+right)//2
                curr_value,next_value = mountain_arr.get(mid),mountain_arr.get(mid+1)
                if(curr_value < next_value):
                    left=mid+1
                else:
                    right=mid-1

            return left

        def increasing_binary_search(target,peak_index):
            left = 0
            right = peak_index
            while(left<=right):

                mid = (left+right)//2
                if(mountain_arr.get(mid)>target):
                    right=mid-1
                elif(mountain_arr.get(mid)<target):
                    left=mid+1
                else:
                    return mid

            return -1
        
        def decreasing_binary_search(target,peak_index):
            left = peak_index
            right = mountain_arr.length()-1

            while(left<=right):

                mid = (left+right)//2
                if(mountain_arr.get(mid)>target):
                    left=mid+1
                elif(mountain_arr.get(mid)<target):
                    right=mid-1
                else:
                    return mid

            return -1

        peak_index = get_peak()
        answer= increasing_binary_search(target,peak_index)
        if(answer==-1):
            answer=decreasing_binary_search(target,peak_index)

        return answer
