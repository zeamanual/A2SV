from collections import defaultdict
n = int(input())
graph = dict()

for line_count in range(n):
    graph[line_count+1] = []
    line = list(map(int,input().split()))

    for col in range(len(line)):
        if(line[col]!=0):
            graph[line_count+1].append(col+1)

for node in graph.keys():
    print(len(graph[node]),*graph[node])
