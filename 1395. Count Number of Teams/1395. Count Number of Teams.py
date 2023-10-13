class Solution:
    def numTeams(self, rating: List[int]) -> int:

        answer = 0

        for i in range(len(rating)):
            bigger_left,smaller_left,bigger_right,smaller_right=0,0,0,0

            for j in range(len(rating)):
                if(rating[j]>rating[i]):
                    bigger_left +=1 if j<i else 0 
                    bigger_right +=1 if j>i else 0
                elif(rating[j]<rating[i]):
                    smaller_left += 1 if j<i else 0
                    smaller_right += 1 if j>i else 0
            answer += bigger_left * smaller_right + bigger_right * smaller_left
        
        return answer
