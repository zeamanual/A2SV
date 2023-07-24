class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
       
        removed = set()
        players = [ i for i in range(1,n+1)]
        index=0

        while(len(removed)<(len(players)-1)):
            count = 0
            while(count<k):
                if(players[index] not in removed):
                    count+=1
                if(count==k):
                    removed.add(players[index])
                index = (index+1)%n
            
        for i in range(n):
            if(players[i] not in removed):
                return players[i]
