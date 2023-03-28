class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        self.count = 0
        self.diff = diff
        merged = []
        for index in range(len(nums1)):
            merged.append(nums1[index]-nums2[index])
        
        self.merge_sort(merged)
        return self.count

    def merge_sort(self,arr):

        if(len(arr)==1):
            return arr
        
        mid = len(arr)//2
        left_sorted = self.merge_sort(arr[:mid])
        right_sorted = self.merge_sort(arr[mid:])

        return self.merge(left_sorted,right_sorted)

    
    def merge(self,left,right):
        merged =[]
        left_ptr=0
        right_ptr = 0
        self.count_valid_pairs(left,right)
        while(left_ptr<len(left) or right_ptr<len(right)):
           
            left_value = left[left_ptr] if left_ptr<len(left) else float('inf')
            right_value = right[right_ptr] if right_ptr<len(right) else float('inf')

            if(left_value<right_value):
                merged.append(left_value)
                left_ptr+=1
            else:
                merged.append(right_value)
                right_ptr+=1

        return merged

    def count_valid_pairs(self,left,right):
        for num in right:
            curr_val = num+self.diff
            curr_count = 0
            start = 0
            end = len(left)-1
            while(start<=end):
   
                mid = start + (end-start)//2

                if(left[mid]<=curr_val):
                    curr_count = mid+1
                    start= mid+1
                else:
                    end=mid-1
            self.count +=curr_count
