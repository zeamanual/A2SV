class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums,0,len(nums)-1)

        return nums[-k]


    def quick_sort(self,nums,left,right):

        if(left>=right):
            return

        pivot = left
        right_bk = right
        left +=1 
        while(left<=right):
            while(left<=right and nums[left] < nums[pivot] ):
                left+=1

            while(right>=left and nums[right] > nums[pivot]):
                right-=1

            if(right>=left):
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

        nums[pivot],nums[right]=nums[right],nums[pivot]
        self.quick_sort(nums,pivot,right-1)
        self.quick_sort(nums,right+1,right_bk)
