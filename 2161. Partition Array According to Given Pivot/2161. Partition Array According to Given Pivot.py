class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        equal_count=0
        lessthan_pivot = []
        greaterthan_pivot=[]

        for num in nums:
            if(num>pivot):
                greaterthan_pivot.append(num)
            elif(num<pivot):
                lessthan_pivot.append(num)
            else:
                equal_count+=1

        for i in range(equal_count):
            lessthan_pivot.append(pivot)
        
        return lessthan_pivot+greaterthan_pivot

