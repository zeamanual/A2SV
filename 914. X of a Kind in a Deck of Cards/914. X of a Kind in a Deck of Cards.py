class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        freq = Counter(deck)
        freq_list = list(freq.values())
        curr_gcd = freq_list[0]

        for count in freq.values():
            curr_gcd =  gcd(curr_gcd,count)

        return True if(curr_gcd > 1) else False
