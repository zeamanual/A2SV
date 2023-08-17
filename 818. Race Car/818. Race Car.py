class Solution:
    def racecar(self, target: int) -> int:
        que = deque()
        que.append((0,1,0))
        answer =float('inf')
        while(que):

            pos,speed,step=que.popleft()
            if(pos==target):
                answer = step
                break
    
            # handling A
            que.append((pos+speed,speed*2,step+1))

            # handling R
            if (pos+speed) < target and speed < 0 or (pos+speed) > target and speed > 0:
                que.append((pos,-1 if speed>0 else 1,step+1 ))

        return answer
