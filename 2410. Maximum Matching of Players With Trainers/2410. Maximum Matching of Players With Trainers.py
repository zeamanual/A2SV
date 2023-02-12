class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        players_size=len(players)
        tr_size=len(trainers)
        ply_ptr=0
        tr_ptr=0
        max_count=0

        while(ply_ptr<players_size and tr_ptr<tr_size):
                if(trainers[tr_ptr]>=players[ply_ptr]):
                    ply_ptr+=1
                    tr_ptr+=1
                    max_count+=1
                else:
                    tr_ptr+=1
        return max_count
