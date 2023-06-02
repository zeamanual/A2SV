class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @lru_cache(None)
        def get_max(index):
            if(index>=len(questions)):
                return 0
            option1 = questions[index][0] + get_max( ( index + 1) + questions[index][1] )
            option2 = get_max(index+1)

            return max(option1,option2)


        return get_max(0)
