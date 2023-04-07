from collections import defaultdict
vertices = int(input())
operations = int(input())
graph = defaultdict(list)

for opp_count in range(operations):
    curr_opp = list(map(int,input().split()))

    if(curr_opp[0]==1):
        graph[curr_opp[1]].append(curr_opp[2])
        graph[curr_opp[2]].append(curr_opp[1])

    else:
        print(*graph[curr_opp[1]])
