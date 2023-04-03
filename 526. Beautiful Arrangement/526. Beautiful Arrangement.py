class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [ i+1 for i in range(n)]
        visited = set()
        count = 0
        def backtrack(index,arr):
            nonlocal count
            if(len(arr) == len(nums)):
                count+=1

            for i in range(len(nums)):

                arr.append(nums[i])
                if( i in visited or (nums[i]%(len(arr)) !=0 and (len(arr))%nums[i] != 0 )):
                    arr.pop()
                    continue

                visited.add(i)
                backtrack(i+1,arr)
                visited.discard(i)
                arr.pop()

        backtrack(0,[])

        return count
