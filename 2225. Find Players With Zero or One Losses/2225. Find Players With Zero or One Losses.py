class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners=set()
        lossers=set()
        only_one_lossers=set()

        for match in matches:

            if(match[1] in only_one_lossers):
                only_one_lossers.discard(match[1])
            elif(match[1] not in lossers):
                if(match[1] in winners):
                    winners.discard(match[1])
                lossers.add(match[1])
                only_one_lossers.add(match[1])
                
            if(match[0] not in winners and match[0] not in lossers):
                winners.add(match[0])

        return [sorted(list(winners)),sorted(list(only_one_lossers))]
