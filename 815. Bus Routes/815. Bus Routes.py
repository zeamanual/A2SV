class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph= defaultdict(list)
        for bus in range(len(routes)):
            
            for bus_stops in routes[bus]:
                graph[bus_stops].append(bus)

        queue = deque([(source, 0)])
        visited_stop = set([source])
        visited_bus = set()
        
        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses
            for bus in graph[stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)

                    for stop in routes[bus]:
                        if stop not in visited_stop:
                            visited_stop.add(stop)
                            queue.append((stop,  buses+1))
        
        return -1
