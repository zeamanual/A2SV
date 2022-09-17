class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        size = len(piles)
        rounds = size//3
        
        for round in range(rounds):
            coins+=piles[((size-1)-(2*round+1))]
            
        return coins
