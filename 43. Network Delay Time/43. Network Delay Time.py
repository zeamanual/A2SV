class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        distances = {node: float('inf') for node in range(1,n+1)}       
        distances[k]=0

        graph = {node: {} for node in range(1,n+1)}

        for edge in times:
            graph[edge[0]][edge[1]]=edge[2]

        distances[k] = 0
        visited = set()
        priority_queue = [(0, k)]
        while priority_queue:
            
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                
        answer = max(distances.values())

        return answer if answer!=float('inf') else -1
