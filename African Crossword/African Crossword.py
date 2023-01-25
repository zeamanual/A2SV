n,m = list(map(int,input().split()))

matr= [['' for j in range(m)] for i in range(n)]

row_info={}
col_info={}
for i in range(n):
    row_info[i]={}
    cur_row=input()
    for j in range(m):
        matr[i][j]=cur_row[j]
        if(j not in col_info):
            col_info[j]={}
        row_info[i][cur_row[j]]=row_info[i].get(cur_row[j],0)+1
        col_info[j][cur_row[j]]=col_info[j].get(cur_row[j],0)+1

final_str=[]
for i in range(n):
    for j in range(m):
        if(row_info[i][matr[i][j]] >1 or col_info[j][matr[i][j]]>1):
            continue
        else:
            final_str.append(matr[i][j])

print(''.join(final_str))
