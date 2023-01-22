class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_size=len(arr)
        
        if(arr_size<3):
            return False
        
        left_ptr=0
        right_ptr=arr_size-1

        for i in range(1,arr_size-1):
            if(arr[i]>arr[i-1]):
                left_ptr+=1
            elif(arr[i]<arr[i-1]):
                break

        for i in range(arr_size-1,1,-1):
            if(arr[i]<arr[i-1]):
                right_ptr-=1
            elif(arr[i]>arr[i-1]):
                break
        
        if(left_ptr==right_ptr):
            return True
        else:
            return False
