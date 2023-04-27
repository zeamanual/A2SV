class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        que = deque([['0000',0]])
        deadends= set(deadends)
        possible_moves = [[0,1],[0,-1],[1,1],[1,-1],[2,1],[2,-1],[3,1],[3,-1]]
        visited = set()

        def apply_move(move,curr):
            curr = list(map(int,list(curr)))
            curr_val = curr[move[0]]+move[1]
            curr[move[0]]= curr_val % 10 if curr_val >= 0 else 9
            return ''.join(map(str,curr))

        while(que):
            curr,turn = que.popleft()
            if(curr==target):
                return turn

            if(curr in deadends):
                continue
            for move in possible_moves:
                new_comb = apply_move(move,curr)
                if(new_comb not in visited):
                    visited.add(new_comb)
                    que.append([new_comb,turn+1])

        return -1
