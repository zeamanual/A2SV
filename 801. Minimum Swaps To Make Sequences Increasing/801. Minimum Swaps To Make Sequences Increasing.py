class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:

        nums1=[-1]+nums1
        nums2=[-1]+nums2

        @lru_cache(None)
        def dp(index,last_one,last_two):

            if(index>=len(nums1)):
               return 0

            option1,option2,option3=float('inf'),float('inf'),float('inf')
            if(nums1[index]<=last_one or nums2[index]<=last_two):
                option1=1+dp(index+1,nums2[index],nums1[index])
            else:
                if(nums2[index]>last_one and nums1[index]>last_two):
                    option2=1+dp(index+1,nums2[index],nums1[index])
                
                if(nums2[index]>last_two and nums1[index]>last_one):
                    option3 = dp(index+1,nums1[index],nums2[index])
            
            return min(option1,option2,option3)
        return dp(1,nums1[0],nums2[0])
