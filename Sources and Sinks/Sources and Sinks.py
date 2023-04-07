from collections import defaultdict
vertices,sources,sinks,graph = int(input()),[],[],dict()

for i in range(vertices):
    graph[i+1]=[]

for line_index in range(vertices):
    curr_line = list(map(int,input().split()))

    for index in range(len(curr_line)):
        if(curr_line[index]>0):
            graph[line_index+1].append(index+1)

for vertice in list(graph.keys()):
    isSource= True
    isSink = True if len(graph[vertice])==0 else False
    for other_vertice in list(graph.keys()):
        if(vertice != other_vertice and vertice in graph[other_vertice] ):
            isSource=False

    if(isSource):
        sources.append(vertice)
    if(isSink):
        sinks.append(vertice)

print(len(sources),*sources)
print(len(sinks),*sinks)
