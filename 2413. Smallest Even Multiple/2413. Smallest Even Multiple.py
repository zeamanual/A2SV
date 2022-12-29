class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        smallest_multiple=n
        while(smallest_multiple%2 !=0):
            smallest_multiple*=2
        
        return smallest_multiple
