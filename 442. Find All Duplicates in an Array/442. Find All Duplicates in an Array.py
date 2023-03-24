class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        index=0
        answer =[]
        while( index < size):
            pos = nums[index]-1
            if( pos == index ):
                index +=1
            elif(nums[pos]==nums[index]):
                answer.append(nums[index])
                nums[index]=-1
                index+=1
            else:
                nums[pos],nums[index]= nums[index] ,nums[pos]
                if(nums[index]==-1):
                    index+=1

        return answer
