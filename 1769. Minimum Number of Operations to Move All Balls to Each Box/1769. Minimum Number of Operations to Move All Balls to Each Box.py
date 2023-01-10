class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        balls_dic = {}
        boxes_size = len(boxes)

        for index,box in enumerate(boxes):
            if(int(box)==1):
                balls_dic[index]=1

        answer = []
        for i in range(boxes_size):
            i_th_answer=0
            for ball_index in balls_dic.keys():
                i_th_answer+=abs(i-ball_index)
            answer.append(i_th_answer)

        return answer
