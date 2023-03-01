class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        total_score =0
        for num in nums:
            total_score+=num
        
        player_1_sum = self.max_player1_score(nums,0,len(nums)-1,1)
        player_2_sum = total_score-player_1_sum
        return player_1_sum>=player_2_sum


    def max_player1_score(self,nums,left,right,turn):
        if(right<left):
            return 0
            
        if(turn ==1):
            return max(nums[left]+self.max_player1_score(nums,left+1,right,0),nums[right]+self.max_player1_score(nums,left,right-1,0))
        else:
            return min(self.max_player1_score(nums,left+1,right,1),self.max_player1_score(nums,left,right-1,1))
