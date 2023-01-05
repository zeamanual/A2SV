class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        rearrenged = []

        array_size = len(nums)
        pst_ptr = 0
        ngt_ptr = 0

        while(pst_ptr < array_size and ngt_ptr < array_size):
            while(nums[ngt_ptr] > 0):
                ngt_ptr+=1

            while(nums[pst_ptr] < 0):
                pst_ptr+=1

            rearrenged.append(nums[pst_ptr])
            rearrenged.append(nums[ngt_ptr])

            pst_ptr+=1
            ngt_ptr+=1


        return rearrenged
