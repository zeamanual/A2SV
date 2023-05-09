class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [(task[0], task[1], index) for index, task in enumerate(tasks)]
        tasks.sort()

        ans, cpu_que = [], []
        i, time = 0, tasks[0][0]
        while i < len(tasks):
            while i<len(tasks) and tasks[i][0] <= time:
                heapq.heappush(cpu_que, [tasks[i][1], tasks[i][2]])
                i+=1
            
            if cpu_que:
                processing_time, idx = heappop(cpu_que)
                ans.append(idx)
                time += processing_time
            else:
                time = tasks[i][0]
        
        while cpu_que:
            processing_time, idx = heappop(cpu_que)
            ans.append(idx)
        return ans
