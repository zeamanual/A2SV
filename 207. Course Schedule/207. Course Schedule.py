class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_stat = [0 for i in range(numCourses)]
        rel = defaultdict(list)
        for cor,pre in prerequisites:
            pre_stat[cor]+=1
            rel[pre].append(cor)

        que = deque()
        for cor_id in range(numCourses):
            if(pre_stat[cor_id]==0):
                que.append(cor_id)

        
        while(que):
            cor_id = que.popleft()
            for cor in rel[cor_id]:
                pre_stat[cor]-=1
                if(pre_stat[cor]==0):
                    que.append(cor)

        for stat in pre_stat:
            if(stat>0):
                return False

        return True
