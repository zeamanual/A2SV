class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dxs = ['north','east','south','west']
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        def get_direction(index):
            
            index%=4
            return index

        curr_direction = 0
        curr_cord = (0,0)
        for inst in instructions:
            if inst=='G':
                curr_cord = (curr_cord[0]+moves[curr_direction][0],curr_cord[1]+moves[curr_direction][1])
            else:
                if(inst=='L'):
                    curr_direction=get_direction(curr_direction+1)
                else:
                    curr_direction=get_direction(curr_direction-1)

        return curr_cord==(0,0) or curr_direction!=0
