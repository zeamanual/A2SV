class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums=self.merge_sort(nums)
        print(nums)
        
        return str(int(''.join(list(map(str,nums)))))

    def merge_sort(self,nums):

        if(len(nums)==1):
            return nums
        else:
            middle=len(nums)//2
            left_sorted=self.merge_sort(nums[:middle])
            right_sorted=self.merge_sort(nums[middle:])

            return self.merge(left_sorted,right_sorted)
        
    def first_greater(self,num1,num2):
        return str(num1)+str(num2)>str(num2)+str(num1)
    
    def merge(self,arr1,arr2):
        ptr1=0
        ptr2=0
        merged=[]
        while(ptr1<len(arr1) and ptr2<len(arr2)):
            if(self.first_greater(arr1[ptr1],arr2[ptr2])):
                merged.append(arr1[ptr1])
                ptr1+=1
            else:
                merged.append(arr2[ptr2])
                ptr2+=1

        while(ptr1<len(arr1)):
            merged.append(arr1[ptr1])
            ptr1+=1    
        while(ptr2<len(arr2)):
            merged.append(arr2[ptr2])
            ptr2+=1

        return merged              

