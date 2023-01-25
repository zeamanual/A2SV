class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        arr_size=len(arr)
        largest_num=float('-inf')
        greatest=[ 0 for i in range(arr_size)]
        
        # storing the gretest element right side of the index
        for index in range(arr_size-1,0,-1):
            if(arr[index]>largest_num):
                largest_num=arr[index]
            
            greatest[index]=largest_num

        final_answer=[]

        for index in range(arr_size-1):
            final_answer.append(greatest[index+1])
        final_answer.append(-1)

        return final_answer
