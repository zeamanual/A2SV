test_cases = int(input())

for i in range(test_cases):
    n,m = list(map(int,input().split()))
    matr = []
    left_dig={}
    right_dig={}
    for row in range(n):
        matr.append([])
        current_row = list(map(int,input().split()))
        for col in range(m):
            matr[row].append(current_row[col])
            left_dig[row-col]=left_dig.get(row-col,0)+matr[row][col]
            right_dig[row+col]=right_dig.get(row+col,0)+matr[row][col]

    max_sum=0
    for row in range(n):
        for col in range(m):
            current_sum=left_dig[row-col]+right_dig[row+col]-matr[row][col]
            max_sum=max(max_sum,current_sum)
          
    print(max_sum)
