class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        arr_size = len(skill)
        left_ptr=0
        right_ptr=arr_size-1

        prev_sum=0
        team_chem=0
        while(left_ptr<right_ptr):
            current_sum=skill[left_ptr]+skill[right_ptr]
            current_prod=skill[left_ptr]*skill[right_ptr]
            if(prev_sum==0):
                prev_sum=current_sum
                team_chem+=current_prod
            elif(current_sum!=prev_sum):
                return -1
            else:
                team_chem+=current_prod
            left_ptr+=1
            right_ptr-=1

        return team_chem
