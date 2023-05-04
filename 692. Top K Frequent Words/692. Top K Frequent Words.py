class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        words = list(map(lambda x:(-x[1],x[0]) , freq.items()))
        heapq.heapify(words)

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(words)[1])
        
        return answer
