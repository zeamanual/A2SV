class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips_pos=[]
        size=len(arr)
        start_index=size-1
        for index in range(start_index,0,-1):
            largest_index = self.findLargestIndex(arr[0:index+1])
            self.flip(arr,largest_index)
            self.flip(arr,index)
            flips_pos.append(largest_index+1)
            flips_pos.append(index+1)
        return flips_pos
            
            
        
    def findLargestIndex(self,arr):
        max=arr[0]
        max_index=0

        for index in range(len(arr)):
            if(arr[index]>max):
                max=arr[index]
                max_index=index
            else:
                continue
        return max_index
    
    def flip(self,arr,last_index):
        middle =last_index//2
        temp_pos=last_index
        
        for index in range(last_index,middle,-1):
            temp = arr[index]
            arr[index]=arr[temp_pos-index]
            arr[temp_pos-index]=temp
        return arr
