from collections import defaultdict


n = int(input())

count = 0
graph = defaultdict(list)
for row_count in range(n):
    
    curr_row = list(map(int,input().split()))

    for col_count in range(len(curr_row)):
        if(curr_row[col_count]==1):
            graph[row_count+1].append(curr_row[col_count])
            count+=1

print(int(count/2))
